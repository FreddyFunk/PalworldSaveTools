@echo off
rem Run the python bootstrapper
python "%~dp0setup.py"
exit /b %errorlevel%
