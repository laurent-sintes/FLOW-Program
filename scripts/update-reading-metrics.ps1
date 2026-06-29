$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$venvPackages = Join-Path $repoRoot ".venv\Lib\site-packages"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$metricsScript = Join-Path $repoRoot "scripts\update_reading_metrics.py"
$isCodexRuntime = ($env:Path -split ";") -match "codex-runtimes|OpenAI\\Codex|\\.codex"
$previousPythonPath = $env:PYTHONPATH

if (-not (Test-Path $metricsScript)) {
    throw "Script de statistiques introuvable : $metricsScript"
}

Push-Location $repoRoot
try {
    if ($isCodexRuntime -and (Test-Path $codexPython) -and (Test-Path $venvPackages)) {
        $env:PYTHONPATH = $venvPackages
        & $codexPython $metricsScript
    }
    elseif (Test-Path $venvPython) {
        & $venvPython $metricsScript
    }
    else {
        python $metricsScript
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Mise a jour des statistiques en erreur : code $LASTEXITCODE"
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
