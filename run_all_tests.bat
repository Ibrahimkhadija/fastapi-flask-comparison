@echo off
echo ========================================
echo RUNNING ALL TESTS
echo ========================================
echo.

echo 1. Testing FastAPI...
cd /d "C:\Users\Hp\Documents\fastapi_project\fastapi_app"
call venv\Scripts\activate
pip install httpx --quiet
echo.
pytest test_api.py -v

echo.
echo 2. Testing Flask...
cd /d "C:\Users\Hp\Documents\fastapi_project\flask_app"
call venv\Scripts\activate
pip install pytest --quiet
echo.
pytest test_app.py -v

echo.
echo ========================================
echo ALL TESTS COMPLETE
echo ========================================
pause