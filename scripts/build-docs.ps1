$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$venvPackages = Join-Path $repoRoot ".venv\Lib\site-packages"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$buildScript = Join-Path $repoRoot "scripts\build_multilang.py"
$isCodexRuntime = ($env:Path -split ";") -match "codex-runtimes|OpenAI\\Codex|\\.codex"
$previousWarningFlag = $env:NO_MKDOCS_2_WARNING
$previousPythonPath = $env:PYTHONPATH

if (-not (Test-Path $venvPython)) {
    throw "Environnement Python introuvable : $venvPython"
}

if (-not (Test-Path $venvPackages)) {
    throw "Packages Python introuvables : $venvPackages"
}

if (-not (Test-Path $buildScript)) {
    throw "Script de build multilingue introuvable : $buildScript"
}

Push-Location $repoRoot
try {
    $env:NO_MKDOCS_2_WARNING = "true"

    if ($isCodexRuntime -and (Test-Path $codexPython)) {
        $env:PYTHONPATH = $venvPackages
        & $codexPython $buildScript
    }
    else {
        & $venvPython $buildScript
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Build MkDocs en erreur : code $LASTEXITCODE"
    }
}
finally {
    if ($null -eq $previousWarningFlag) {
        Remove-Item Env:NO_MKDOCS_2_WARNING -ErrorAction SilentlyContinue
    }
    else {
        $env:NO_MKDOCS_2_WARNING = $previousWarningFlag
    }

    if ($null -eq $previousPythonPath) {
        Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONPATH = $previousPythonPath
    }

    Pop-Location
}
