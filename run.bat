@echo off
title AgriVoice Vision - Kisan AI Diagnostic System
echo Starting AgriVoice Vision...
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
    streamlit run app.py
) else (
    python -m streamlit run app.py
)
pause
