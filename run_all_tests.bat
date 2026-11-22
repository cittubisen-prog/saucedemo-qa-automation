@echo off
title Complete QA Test Suite - UI + API
color 0E
cd /d "%~dp0"
echo ============================================================
echo   RUNNING FULL AUTOMATED TEST SUITE (15 Tests)
echo   Part 3 (UI Automation) + Part 4 (API Automation)
echo   Candidate: Vishwa Vijay Kumar
echo ============================================================
echo.
python -m pytest -v
echo.
echo ============================================================
echo   Full Test Suite Finished!
echo ============================================================
pause
