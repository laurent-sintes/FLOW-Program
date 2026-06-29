$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$venvPackages = Join-Path $repoRoot ".venv\Lib\site-packages"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$checkScript = Join-Path $repoRoot "scripts\check_site.py"
$isCodexRuntime = ($env:Path -split ";") -match "codex-runtimes|OpenAI\\Codex|\\.codex"
$previousPythonPath = $env:PYTHONPATH

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
        & $codexPython $checkScript
    }
    else {
        & $venvPython $checkScript
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
