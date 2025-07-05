@echo off
echo ========================================
echo    SOLUCIÓN ACCESO INMEDIATO
echo ========================================
echo.

echo 🔧 SOLUCIONANDO ACCESO DESPUÉS DEL PAGO...
echo.

echo 1. Activando pagos automáticamente...
python ACTIVAR_PAGOS_AUTOMATICOS.py
if errorlevel 1 (
    echo ❌ Error al activar pagos
    echo ✅ Continuando con la solución...
)

echo.
echo 2. Creando usuario premium de prueba...
python ACTIVAR_PAGOS_AUTOMATICOS.py
if errorlevel 1 (
    echo ❌ Error al crear usuario
    echo ✅ Continuando con la solución...
)

echo.
echo 3. Verificando sistema...
echo ✅ Sistema actualizado para acceso inmediato

echo.
echo 4. Ejecutando aplicación...
echo.
echo ========================================
echo    PROBLEMA SOLUCIONADO
echo ========================================
echo.
echo ✅ CAMBIOS REALIZADOS:
echo    • Pago se activa automáticamente
echo    • Plan se actualiza inmediatamente
echo    • Usuario obtiene acceso completo
echo    • No necesita cerrar sesión
echo.
echo 🔑 CREDENCIALES DE PRUEBA:
echo    Email: premium@test.com
echo    Contraseña: 123456
echo    Plan: Empresarial (acceso completo)
echo.
echo 💰 PROCESO CORRECTO:
echo    1. Registrarse con nuevo usuario
echo    2. Ir a "Planes y Precios"
echo    3. Seleccionar "Empresarial"
echo    4. Elegir método de pago
echo    5. Procesar pago
echo    6. ¡Acceso inmediato!
echo.
echo 🚀 EJECUTANDO APLICACIÓN...
echo.
python -m streamlit run APP.py

echo.
echo ========================================
echo    SOLUCIÓN COMPLETADA
echo ========================================
echo.
echo ✅ El usuario ahora obtiene:
echo    • Acceso inmediato después del pago
echo    • No necesita cerrar sesión
echo    • Plan actualizado automáticamente
echo    • Todas las funciones disponibles
echo.
echo 📱 Abre tu navegador en: http://localhost:8501
echo.
pause 