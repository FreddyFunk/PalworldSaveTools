@echo off
rem Run the python bootstrapper
python "%~dp0setup_pst.py"
exit /b %errorlevel%