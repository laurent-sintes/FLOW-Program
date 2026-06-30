$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$generatorScript = Join-Path $repoRoot "scripts\generate_svg_diagrams.py"
$isCodexRuntime = ($env:Path -split ";") -match "codex-runtimes|OpenAI\\Codex|\\.codex"

if (-not (Test-Path $generatorScript)) {
    throw "Script de generation SVG introuvable : $generatorScript"
}

Push-Location $repoRoot
try {
    if ($isCodexRuntime -and (Test-Path $codexPython)) {
        & $codexPython $generatorScript
    }
    elseif (Test-Path $venvPython) {
        & $venvPython $generatorScript
    }
    else {
        python $generatorScript
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Generation des SVG en erreur : code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
