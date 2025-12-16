@echo off
echo ========================================
echo SETTING UP GIT REPOSITORY
echo ========================================
echo.

cd /d "C:\Users\Hp\Documents\fastapi_project"

echo Step 1: Checking current location...
echo Current directory: %CD%
echo.

echo Step 2: Initializing git repository...
if exist ".git" (
    echo .git folder already exists
    echo Removing and starting fresh...
    rmdir /s .git
)
git init
echo ✓ Git repository initialized
echo.

echo Step 3: Configuring git...
git config user.name "Ibrahimkhadija"
git config user.email "ibrahimkhadija@example.com"
echo ✓ Git configured
echo.

echo Step 4: Adding files to git...
git add .
echo ✓ Files added to staging
echo.

echo Step 5: Committing changes...
git commit -m "FastAPI vs Flask comparison project - Complete implementation"
echo ✓ Changes committed
echo.

echo Step 6: Connecting to GitHub...
git remote add origin https://github.com/Ibrahimkhadija/fastapi-flask-comparison.git
echo ✓ Connected to GitHub
echo.

echo Step 7: Pushing to GitHub...
git branch -M main
git push -u origin main
echo.

if errorlevel 1 (
    echo ❌ Push failed!
    echo.
    echo Common solutions:
    echo 1. If repository exists on GitHub: git pull origin main --allow-unrelated-histories
    echo 2. Then: git push origin main
    echo 3. Or force push: git push -f origin main (WARNING: overwrites GitHub)
) else (
    echo ✅ SUCCESS! Project pushed to GitHub
    echo.
    echo Repository URL: https://github.com/Ibrahimkhadija/fastapi-flask-comparison
)

echo.
echo ========================================
pause