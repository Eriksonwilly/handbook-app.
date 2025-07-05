@echo off
echo ========================================
echo   CONSORCIO DEJ - ACTIVACION ADMIN
echo ========================================
echo.
echo Activando acceso completo para administrador...
echo.

REM Verificar si existe el entorno virtual
if exist "venv\Scripts\activate.bat" (
    echo [1/4] Activando entorno virtual...
    call venv\Scripts\activate.bat
) else (
    echo [1/4] Creando entorno virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo [2/4] Instalando dependencias...
pip install streamlit pandas numpy matplotlib plotly reportlab

echo [3/4] Ejecutando script de activación...
python ACTIVAR_ADMIN_COMPLETO.py

echo [4/4] Iniciando aplicación principal...
echo.
echo ========================================
echo   ACCESO COMPLETO ACTIVADO
echo ========================================
echo.
echo Credenciales de Administrador:
echo - Usuario: admin
echo - Contraseña: admin123
echo - Plan: Empresarial (acceso completo)
echo.
echo La aplicación se abrirá en tu navegador...
echo.
pause
streamlit run APP.py 