# Environment setup

## Requirements
- Python 3.10 or newer.
- pip and a terminal (PowerShell, Command Prompt, macOS Terminal, or Linux shell).
- Internet access for the first dependency installation.

## Create an isolated environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can invoke the environment's Python directly with `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`; avoid changing machine-wide execution policy just for this project.

On macOS/Linux, activate with `source .venv/bin/activate`.

## Verify setup

```bash
python --version
python -m pytest
python examples/search/bfs.py
python examples/ml/linear_regression.py
```

## Common fixes
- **ModuleNotFoundError:** activate the environment and install requirements using the same Python interpreter.
- **Wrong interpreter in VS Code:** use “Python: Select Interpreter” and choose the repository's `.venv`.
- **Plot window does not open:** some environments are headless; examples should still be understandable from their printed output. Save plots to a local folder only when the script explicitly supports it.
- **Package install fails:** record the full error and Python version before troubleshooting.

Legacy root scripts may have different dependency requirements and may be interactive. Check their imports before running them.
