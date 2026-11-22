@echo off
title Live UI Automation Tests - SauceDemo
color 0B
cd /d "%~dp0"
echo ============================================================
echo   LIVE UI AUTOMATION TESTS (https://www.saucedemo.com)
echo   Framework: Selenium WebDriver + Page Object Model
echo   Candidate: Vishwa Vijay Kumar
echo ============================================================
echo.
python -m pytest tests/test_saucedemo_ui.py -v
echo.
echo ============================================================
echo   UI Tests Finished!
echo ============================================================
pause
