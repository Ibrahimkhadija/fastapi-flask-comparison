@echo off
echo Setting up test environment...
echo.

REM Activate venv
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Could not activate venv!
    echo Make sure you're in fastapi_app folder
    pause
    exit /b 1
)

echo Installing test dependencies...
pip install httpx pytest requests

echo.
echo Verifying installations...
python -c "import httpx; print('✓ httpx installed')"
python -c "import pytest; print('✓ pytest installed')"
python -c "import requests; print('✓ requests installed')"

echo.
echo Running tests...
pytest test_api.py -v

echo.
pause