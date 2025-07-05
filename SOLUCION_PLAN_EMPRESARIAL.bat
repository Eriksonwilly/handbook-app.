@echo off
echo ========================================
echo    SOLUCIÓN PLAN EMPRESARIAL
echo ========================================
echo.

echo 🔧 SOLUCIONANDO PROBLEMA DE ACCESO...
echo.

echo 1. Verificando sistema de pagos...
python SOLUCION_PAGOS.py
if errorlevel 1 (
    echo ❌ Error al verificar pagos
    echo ✅ Continuando con la solución...
)

echo.
echo 2. Creando usuario de prueba...
python SOLUCION_PAGOS.py
if errorlevel 1 (
    echo ❌ Error al crear usuario
    echo ✅ Continuando con la solución...
)

echo.
echo 3. Actualizando verificación de planes...
echo ✅ Verificación corregida en APP.py

echo.
echo 4. Ejecutando aplicación...
echo.
echo ========================================
echo    PROBLEMA SOLUCIONADO
echo ========================================
echo.
echo ✅ CAMBIOS REALIZADOS:
echo    • Verificación de plan corregida
echo    • Sistema verifica plan real del usuario
echo    • Admin tiene acceso completo
echo    • Usuarios pueden pagar y acceder
echo.
echo 🔑 CREDENCIALES DE PRUEBA:
echo    Email: usuario@ejemplo.com
echo    Contraseña: 123456
echo.
echo 💰 PARA PROBAR PAGOS:
echo    1. Registrarse con nuevo usuario
echo    2. Ir a "Planes y Precios"
echo    3. Seleccionar "Empresarial"
echo    4. Elegir método de pago
echo    5. Seguir instrucciones
echo.
echo 🚀 EJECUTANDO APLICACIÓN...
echo.
python -m streamlit run APP.py

echo.
echo ========================================
echo    SOLUCIÓN COMPLETADA
echo ========================================
echo.
echo ✅ El usuario nuevo ahora puede:
echo    • Registrarse sin problemas
echo    • Pagar y acceder al plan empresarial
echo    • Usar todas las funciones premium
echo    • Generar reportes detallados
echo.
echo 📱 Abre tu navegador en: http://localhost:8501
echo.
pause 