# CONSORCIO DEJ - INSTALACION COMPLETA
# Script de PowerShell para instalar y ejecutar la aplicación

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   CONSORCIO DEJ - INSTALACION COMPLETA" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[1/5] Verificando Python..." -ForegroundColor Green
    Write-Host $pythonVersion -ForegroundColor Yellow
} catch {
    Write-Host "ERROR: Python no está instalado o no está en el PATH" -ForegroundColor Red
    Write-Host "Por favor instala Python desde: https://python.org" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

# Crear entorno virtual si no existe
if (-not (Test-Path "venv")) {
    Write-Host "[2/5] Creando entorno virtual..." -ForegroundColor Green
    python -m venv venv
} else {
    Write-Host "[2/5] Entorno virtual ya existe..." -ForegroundColor Yellow
}

# Activar entorno virtual
Write-Host "[3/5] Activando entorno virtual..." -ForegroundColor Green
& "venv\Scripts\Activate.ps1"

# Instalar dependencias
Write-Host "[4/5] Instalando dependencias..." -ForegroundColor Green
pip install --upgrade pip
pip install streamlit
pip install pandas
pip install numpy
pip install matplotlib
pip install plotly
pip install reportlab
pip install openpyxl

Write-Host "[5/5] Iniciando aplicacion..." -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   CREDENCIALES DE ADMINISTRADOR" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usuario: admin" -ForegroundColor Yellow
Write-Host "Contraseña: admin123" -ForegroundColor Yellow
Write-Host "Plan: Empresarial (acceso completo)" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   FUNCIONES DISPONIBLES" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✅ Análisis completo" -ForegroundColor Green
Write-Host "✅ Diseño del fuste" -ForegroundColor Green
Write-Host "✅ Reportes PDF" -ForegroundColor Green
Write-Host "✅ Gráficos avanzados" -ForegroundColor Green
Write-Host "✅ Todas las funciones premium" -ForegroundColor Green
Write-Host ""
Write-Host "La aplicación se abrirá en tu navegador..." -ForegroundColor Yellow
Write-Host ""
Read-Host "Presiona Enter para continuar"

# Ejecutar la aplicación
streamlit run APP.py 