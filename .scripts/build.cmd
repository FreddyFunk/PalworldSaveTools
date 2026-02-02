@echo off
title PalworldSaveTools Exe Builder
cd /d "%~dp0.."
echo ========================================
echo PalworldSaveTools Exe Builder
echo ========================================
echo Now building the .exe...
python .scripts\build.py %*
echo Exe building completed!
echo All done! Enjoy your latest PST Exe!
pause
