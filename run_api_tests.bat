@echo off
title Live API Automation Tests - Reqres.in
color 0A
cd /d "%~dp0"
echo ============================================================
echo   LIVE API AUTOMATION TESTS (https://reqres.in)
echo   Target: Reqres REST API
echo   Candidate: Vishwa Vijay Kumar
echo ============================================================
echo.
python -m pytest tests/test_reqres_api.py -v -s
echo.
echo ============================================================
echo   API Tests Finished!
echo ============================================================
pause
