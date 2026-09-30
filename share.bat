@echo off
title AgriVoice Vision - Public Web Share Tunnel
echo =========================================================
echo   🌾 AgriVoice Vision - Public Web Share Tunnel
echo =========================================================
echo.
echo Connecting to secure HTTPS public relay for Streamlit (Port 8501)...
echo Share the generated HTTPS link with anyone on any device!
echo.
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=30 -p 443 -R0:localhost:8501 a.pinggy.io
pause
