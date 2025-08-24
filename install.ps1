# Step 1: Check for Python
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python not found. Installing..."
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe" -OutFile "python-installer.exe"
    Start-Process "python-installer.exe" -Wait -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1"
    Remove-Item "python-installer.exe"
} else {
    Write-Host "✅ Python found"
}

# Step 2: Create Virtual Environment
if (-Not (Test-Path ".\venv")) {
    python -m venv venv
    Write-Host "✅ Virtual environment created"
}

# Step 3: Activate venv & install requirements
& .\venv\Scripts\Activate.ps1
Write-Host "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Launch the app
Write-Host "🚀 Launching LexiAI..."
python main.py
