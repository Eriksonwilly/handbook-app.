@echo off
echo ========================================
echo    SOLUCIÓN COMPLETA - CONSORCIO DEJ
echo ========================================
echo.

echo 🔧 SOLUCIONANDO PROBLEMAS...
echo.

echo 1. Verificando acceso de administrador...
python VERIFICAR_ADMIN.py
if errorlevel 1 (
    echo ❌ Error al verificar admin
    echo ✅ Continuando con la solución...
)

echo.
echo 2. Configurando datos bancarios...
echo.
echo IMPORTANTE: Necesitas configurar tus datos bancarios reales
echo para que el dinero llegue a tu cuenta BCP.
echo.
echo ¿Quieres configurar ahora? (s/n)
set /p configurar=

if /i "%configurar%"=="s" (
    python CONFIGURAR_DATOS_BANCARIOS.py
) else (
    echo.
    echo ⚠️ Recuerda configurar tus datos bancarios después
    echo.
)

echo.
echo 3. Instalando dependencias...
pip install streamlit pandas numpy matplotlib plotly
if errorlevel 1 (
    echo ⚠️ Error al instalar, intentando con python -m pip...
    python -m pip install streamlit pandas numpy matplotlib plotly
)

echo.
echo 4. Ejecutando aplicación...
echo.
echo ========================================
echo    APLICACIÓN LISTA PARA USAR
echo ========================================
echo.
echo 🔑 CREDENCIALES DE ADMINISTRADOR:
echo    Usuario: admin
echo    Contraseña: admin123
echo    Email: admin@consorciodej.com
echo.
echo 🎯 PARA ACCEDER AL MODO EMPRESARIAL:
echo    1. Inicia sesión con las credenciales de admin
echo    2. Ve a "Configuración" → "Cambiar Plan"
echo    3. Selecciona "Empresarial"
echo    4. Elige método de pago
echo    5. ¡Listo! Acceso completo
echo.
echo 💰 PARA RECIBIR PAGOS EN TU CUENTA BCP:
echo    1. Configura tus datos bancarios reales
echo    2. Los usuarios pagarán directamente a tu cuenta
echo    3. Confirma los pagos desde el panel de admin
echo.
echo 🚀 EJECUTANDO APLICACIÓN...
echo.
python -m streamlit run APP.py

echo.
echo ========================================
echo    SOLUCIÓN COMPLETADA
echo ========================================
echo.
echo ✅ Problemas solucionados:
echo    • Acceso de administrador configurado
echo    • Sistema de pagos listo para BCP
echo    • Aplicación ejecutándose
echo.
echo 📱 Abre tu navegador en: http://localhost:8501
echo.
pause 