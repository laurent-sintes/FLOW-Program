param(
    [switch]$ExternalLinks,
    [switch]$StrictExternalLinks,
    [ValidateRange(1, 60)]
    [int]$ExternalTimeoutSeconds = 8
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$venvPackages = Join-Path $repoRoot ".venv\Lib\site-packages"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$checkScript = Join-Path $repoRoot "scripts\check_site.py"
$isCodexRuntime = @($env:Path -split ";" | Where-Object { $_ -match "codex-runtimes|OpenAI\\Codex|\\.codex" }).Count -gt 0
$previousPythonPath = $env:PYTHONPATH
$checkArgs = @()
$externalChecksRequested = $ExternalLinks -or $StrictExternalLinks
$canRunExternalChecks = $externalChecksRequested -and -not $isCodexRuntime

if ($externalChecksRequested -and $isCodexRuntime) {
    Write-Warning "Controle des liens externes ignore depuis Codex : le runtime embarque peut bloquer HTTPS. Lancez cette option depuis un PowerShell Windows classique."
}

if ($canRunExternalChecks) {
    $checkArgs += "--external-links"
    $checkArgs += "--external-timeout"
    $checkArgs += $ExternalTimeoutSeconds.ToString([System.Globalization.CultureInfo]::InvariantCulture)
}

if ($StrictExternalLinks -and $canRunExternalChecks) {
    $checkArgs += "--strict-external-links"
}

if (-not (Test-Path $checkScript)) {
    throw "Script de controle introuvable : $checkScript"
}

if (-not (Test-Path $venvPython)) {
    throw "Environnement Python introuvable : $venvPython"
}

if (-not (Test-Path $venvPackages)) {
    throw "Packages Python introuvables : $venvPackages"
}

Push-Location $repoRoot
try {
    & (Join-Path $repoRoot "scripts\build-docs.ps1")

    if ($LASTEXITCODE -ne 0) {
        throw "Build MkDocs en erreur : code $LASTEXITCODE"
    }

    if ($isCodexRuntime -and (Test-Path $codexPython)) {
        $env:PYTHONPATH = $venvPackages
        & $codexPython $checkScript @checkArgs
    }
    else {
        & $venvPython $checkScript @checkArgs
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Controles du site en erreur : code $LASTEXITCODE"
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
