@echo off
title Live API Automation Network Trace (Reqres.in)
color 0A
cd /d "%~dp0"
echo ============================================================
echo   WATCH LIVE API NETWORK REQUESTS & RESPONSES!
echo   Target: https://reqres.in
echo   You will see:
echo     1. Request Method and Endpoints (GET, POST, PUT)
echo     2. JSON Payloads sent across the wire
echo     3. Live Response Times (Latency in milliseconds)
echo     4. Exact Server Status Codes (200, 201, 400, 404)
echo     5. Full Response JSON Bodies & Field Assertions
echo ============================================================
echo.
python run_visual_api_test.py
echo.
pause
