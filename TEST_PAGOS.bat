@echo off
echo ========================================
echo   TEST SISTEMA DE PAGOS - CONSORCIO DEJ
echo ========================================
echo.
echo Ejecutando test completo del sistema...
echo.

python TEST_PAGOS_COMPLETO.py

echo.
echo ========================================
echo   TEST COMPLETADO
echo ========================================
echo.
echo Si todo está OK, ejecuta:
echo streamlit run APP.py
echo.
pause 