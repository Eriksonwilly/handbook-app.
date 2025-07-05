Write-Host "========================================" -ForegroundColor Green
Write-Host "    INSTALACION COMPLETA - CONSORCIO DEJ" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Verificar Python
Write-Host "Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python no está instalado" -ForegroundColor Red
    Write-Host "Instala Python desde: https://python.org" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "Instalando Streamlit..." -ForegroundColor Yellow
try {
    pip install streamlit
    Write-Host "Streamlit instalado correctamente" -ForegroundColor Green
} catch {
    Write-Host "Intentando con python -m pip..." -ForegroundColor Yellow
    python -m pip install streamlit
}

Write-Host ""
Write-Host "Instalando dependencias adicionales..." -ForegroundColor Yellow
pip install pandas numpy matplotlib plotly

Write-Host ""
Write-Host "Verificando instalación..." -ForegroundColor Yellow
pip list | Select-String "streamlit"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "    INSTALACION COMPLETADA" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Para ejecutar la aplicación:" -ForegroundColor Cyan
Write-Host "streamlit run APP.py" -ForegroundColor White
Write-Host ""
Write-Host "Credenciales:" -ForegroundColor Cyan
Write-Host "Usuario: admin" -ForegroundColor White
Write-Host "Contraseña: admin123" -ForegroundColor White
Write-Host ""
Write-Host "Si tienes problemas, ejecuta:" -ForegroundColor Cyan
Write-Host "python -m streamlit run APP.py" -ForegroundColor White
Write-Host ""
Read-Host "Presiona Enter para continuar" 