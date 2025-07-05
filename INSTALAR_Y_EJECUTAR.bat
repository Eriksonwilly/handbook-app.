@echo off
echo ========================================
echo   CONSORCIO DEJ - INSTALACION COMPLETA
echo ========================================
echo.
echo Instalando dependencias y ejecutando aplicacion...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python desde: https://python.org
    pause
    exit /b 1
)

echo [1/5] Verificando Python...
python --version

REM Crear entorno virtual si no existe
if not exist "venv" (
    echo [2/5] Creando entorno virtual...
    python -m venv venv
) else (
    echo [2/5] Entorno virtual ya existe...
)

REM Activar entorno virtual
echo [3/5] Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo [4/5] Instalando dependencias...
pip install --upgrade pip
pip install streamlit
pip install pandas
pip install numpy
pip install matplotlib
pip install plotly
pip install reportlab
pip install openpyxl

echo [5/5] Iniciando aplicacion...
echo.
echo ========================================
echo   CREDENCIALES DE ADMINISTRADOR
echo ========================================
echo.
echo Usuario: admin
echo Contraseña: admin123
echo Plan: Empresarial (acceso completo)
echo.
echo ========================================
echo   FUNCIONES DISPONIBLES
echo ========================================
echo.
echo ✅ Análisis completo
echo ✅ Diseño del fuste
echo ✅ Reportes PDF
echo ✅ Gráficos avanzados
echo ✅ Todas las funciones premium
echo.
echo La aplicación se abrirá en tu navegador...
echo.
pause

streamlit run APP.py 