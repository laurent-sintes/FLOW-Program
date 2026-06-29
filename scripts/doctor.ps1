param(
    [switch]$Network
)

$ErrorActionPreference = "Continue"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$venvPackages = Join-Path $repoRoot ".venv\Lib\site-packages"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$isCodexRuntime = @($env:Path -split ";" | Where-Object { $_ -match "codex-runtimes|OpenAI\\Codex|\\.codex" }).Count -gt 0
$previousPythonPath = $env:PYTHONPATH
$errorCount = 0
$warningCount = 0

function Write-DoctorResult {
    param(
        [ValidateSet("OK", "WARN", "ERROR")]
        [string]$Level,
        [string]$Message
    )

    if ($Level -eq "ERROR") {
        $script:errorCount += 1
    }

    if ($Level -eq "WARN") {
        $script:warningCount += 1
    }

    Write-Host "[$Level] $Message"
}

function Test-RequiredPath {
    param(
        [string]$Path,
        [string]$Label
    )

    if (Test-Path $Path) {
        Write-DoctorResult "OK" "$Label trouve : $Path"
    }
    else {
        Write-DoctorResult "ERROR" "$Label introuvable : $Path"
    }
}

function Invoke-DoctorCommand {
    param(
        [string]$Label,
        [scriptblock]$Command,
        [switch]$Required
    )

    try {
        $output = & $Command 2>&1
        $exitCode = $LASTEXITCODE

        if ($null -eq $exitCode) {
            $exitCode = 0
        }

        if ($exitCode -eq 0) {
            $firstLine = ($output | Select-Object -First 1)
            if ($firstLine) {
                Write-DoctorResult "OK" "$Label : $firstLine"
            }
            else {
                Write-DoctorResult "OK" $Label
            }
        }
        elseif ($Required) {
            Write-DoctorResult "ERROR" "$Label en erreur : code $exitCode"
        }
        else {
            Write-DoctorResult "WARN" "$Label indisponible : code $exitCode"
        }
    }
    catch {
        if ($Required) {
            Write-DoctorResult "ERROR" "$Label en erreur : $($_.Exception.Message)"
        }
        else {
            Write-DoctorResult "WARN" "$Label indisponible : $($_.Exception.Message)"
        }
    }
    finally {
        $global:LASTEXITCODE = 0
    }
}

Write-Host "FLOW environment doctor"
Write-Host "======================="

Push-Location $repoRoot
try {
    Write-DoctorResult "OK" "Racine du projet : $repoRoot"

    if ($isCodexRuntime) {
        Write-DoctorResult "WARN" "Contexte Codex detecte : certains executables du profil Windows peuvent etre bloques par la sandbox."
    }
    else {
        Write-DoctorResult "OK" "Contexte PowerShell Windows classique detecte."
    }

    Test-RequiredPath (Join-Path $repoRoot "mkdocs.yml") "Configuration MkDocs"
    Test-RequiredPath (Join-Path $repoRoot "requirements.txt") "Fichier requirements"
    Test-RequiredPath (Join-Path $repoRoot ".gitattributes") "Configuration Git des fins de ligne"
    Test-RequiredPath (Join-Path $repoRoot ".github\workflows\github-pages.yml") "Workflow GitHub Pages"
    Test-RequiredPath (Join-Path $repoRoot "scripts\build-docs.ps1") "Script de build"
    Test-RequiredPath (Join-Path $repoRoot "scripts\check-site.ps1") "Script de controle"
    Test-RequiredPath (Join-Path $repoRoot "scripts\update-reading-metrics.ps1") "Script de metriques"
    Test-RequiredPath $venvPython "Python du .venv"
    Test-RequiredPath $venvPackages "Packages du .venv"

    Invoke-DoctorCommand "Git" { git --version } -Required
    Invoke-DoctorCommand "Etat Git" { git status -sb } -Required

    if (Get-Command gh -ErrorAction SilentlyContinue) {
        Invoke-DoctorCommand "GitHub CLI" { gh auth status } 
    }
    else {
        Write-DoctorResult "WARN" "GitHub CLI introuvable dans le PATH."
    }

    if ($isCodexRuntime -and (Test-Path $codexPython) -and (Test-Path $venvPackages)) {
        $env:PYTHONPATH = $venvPackages
        Invoke-DoctorCommand "Python utilisable depuis Codex" { & $codexPython -c "import sys, mkdocs, yaml; print(sys.version.split()[0])" } -Required
    }
    elseif (Test-Path $venvPython) {
        Invoke-DoctorCommand "Python du projet" { & $venvPython -c "import sys, mkdocs, yaml; print(sys.version.split()[0])" } -Required
    }
    else {
        Write-DoctorResult "ERROR" "Aucun Python projet utilisable trouve."
    }

    if ($Network) {
        if ($isCodexRuntime) {
            Write-DoctorResult "WARN" "Controle reseau demande depuis Codex : le runtime embarque peut bloquer HTTPS."
        }

        Invoke-DoctorCommand "Acces HTTPS GitHub" {
            $response = Invoke-WebRequest -Uri "https://github.com" -Method Head -TimeoutSec 10
            "HTTP $($response.StatusCode)"
        }
    }
    else {
        Write-DoctorResult "OK" "Controle reseau ignore. Utiliser -Network depuis PowerShell classique si necessaire."
    }
}
finally {
    if ($null -eq $previousPythonPath) {
        Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONPATH = $previousPythonPath
    }

    Pop-Location
}

Write-Host ""
Write-Host "Summary: $errorCount error(s), $warningCount warning(s)"

if ($errorCount -gt 0) {
    exit 1
}

exit 0
