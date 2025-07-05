@echo off
echo ========================================
echo    EJECUTANDO APP - CONSORCIO DEJ
echo ========================================
echo.

echo Verificando si streamlit esta instalado...
pip list | findstr streamlit >nul
if errorlevel 1 (
    echo Streamlit no encontrado. Instalando...
    pip install streamlit
    if errorlevel 1 (
        echo Intentando con python -m pip...
        python -m pip install streamlit
    )
)

echo.
echo Intentando ejecutar la aplicacion...
echo.

REM Intentar diferentes formas de ejecutar streamlit
echo Opcion 1: streamlit run APP.py
streamlit run APP.py
if errorlevel 1 (
    echo.
    echo Opcion 2: python -m streamlit run APP.py
    python -m streamlit run APP.py
    if errorlevel 1 (
        echo.
        echo Opcion 3: python -m streamlit run APP.py --server.port 8501
        python -m streamlit run APP.py --server.port 8501
        if errorlevel 1 (
            echo.
            echo ERROR: No se pudo ejecutar la aplicacion
            echo.
            echo Soluciones:
            echo 1. Ejecuta INSTALAR_TODO.bat primero
            echo 2. Verifica que Python este instalado
            echo 3. Verifica que estes en la carpeta correcta
            echo.
            pause
            exit /b 1
        )
    )
)

echo.
echo ========================================
echo    APLICACION EJECUTADA EXITOSAMENTE
echo ========================================
echo.
echo Abre tu navegador en: http://localhost:8501
echo.
echo Credenciales:
echo Usuario: admin
echo Contraseña: admin123
echo.
pause 