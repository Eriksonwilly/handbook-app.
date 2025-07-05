@echo off
echo ========================================
echo    INSTALACION COMPLETA - CONSORCIO DEJ
echo ========================================
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Instala Python desde: https://python.org
    pause
    exit /b 1
)

echo.
echo Instalando Streamlit...
pip install streamlit
if errorlevel 1 (
    echo Intentando con python -m pip...
    python -m pip install streamlit
)

echo.
echo Instalando dependencias adicionales...
pip install pandas numpy matplotlib plotly

echo.
echo Verificando instalacion...
pip list | findstr streamlit

echo.
echo ========================================
echo    INSTALACION COMPLETADA
echo ========================================
echo.
echo Para ejecutar la aplicacion:
echo streamlit run APP.py
echo.
echo Credenciales:
echo Usuario: admin
echo Contraseña: admin123
echo.
echo Si tienes problemas, ejecuta:
echo python -m streamlit run APP.py
echo.
pause 