@echo off
set currentPath=%cd%
cmd /c "cd /d %currentPath%"
poetry install
py -m pip install pyautogui python-dotenv
exit /b 0         