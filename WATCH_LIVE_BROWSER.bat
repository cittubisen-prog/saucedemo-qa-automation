@echo off
title Live Visual Selenium Automation Demo (Watch Chrome Pop Up)
color 0B
cd /d "%~dp0"
echo ============================================================
echo   WATCH LIVE UI AUTOMATION ON YOUR SCREEN!
echo   Google Chrome will open automatically in full window.
echo   You will see:
echo     1. Auto Login (standard_user)
echo     2. Live Catalog & Price Sorting (Low to High)
echo     3. Adding items to cart & Badge Count
echo     4. Checkout Form auto-fill (Vishwa Kumar)
echo     5. Order Confirmation
echo     6. BUG Demo (problem_user broken images)
echo ============================================================
echo.
python run_visual_browser_test.py
echo.
pause
