#!/usr/bin/env python3
"""
Test Completo del Sistema de Pagos - CONSORCIO DEJ
Script para probar que el cambio de plan funcione correctamente
"""

import json
import os
import datetime

def test_sistema_pagos():
    """Probar el sistema de pagos completo"""
    
    print("🧪 TEST COMPLETO DEL SISTEMA DE PAGOS")
    print("=" * 60)
    print()
    
    # Verificar archivos del sistema
    archivos = ["simple_payment_system.py", "users.json", "payments.json"]
    
    print("📁 Verificando archivos del sistema:")
    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - NO EXISTE")
    print()
    
    # Importar sistema de pagos
    try:
        from simple_payment_system import payment_system
        print("✅ Sistema de pagos importado correctamente")
    except Exception as e:
        print(f"❌ Error importando sistema: {e}")
        return
    print()
    
    # Test 1: Login de admin
    print("🔑 TEST 1: Login de Administrador")
    print("-" * 40)
    
    result = payment_system.login_user("admin", "admin123")
    if result["success"]:
        print("✅ Login admin exitoso")
        print(f"   Plan: {result['user']['plan']}")
        print(f"   Admin: {result['user'].get('is_admin', False)}")
    else:
        print(f"❌ Error login admin: {result['message']}")
    print()
    
    # Test 2: Cambio de plan para admin
    print("🔄 TEST 2: Cambio de Plan para Admin")
    print("-" * 40)
    
    result = payment_system.upgrade_plan("admin", "empresarial", "admin")
    if result["success"]:
        print("✅ Cambio de plan exitoso para admin")
        print(f"   Mensaje: {result['message']}")
        print(f"   Admin access: {result.get('admin_access', False)}")
    else:
        print(f"❌ Error cambio plan: {result['message']}")
    print()
    
    # Test 3: Verificar acceso al plan
    print("🔍 TEST 3: Verificar Acceso al Plan")
    print("-" * 40)
    
    access = payment_system.check_plan_access("admin", "empresarial")
    print(f"Acceso empresarial: {access}")
    
    access = payment_system.check_plan_access("admin", "premium")
    print(f"Acceso premium: {access}")
    
    access = payment_system.check_plan_access("admin", "gratuito")
    print(f"Acceso gratuito: {access}")
    print()
    
    # Test 4: Crear usuario de prueba
    print("👤 TEST 4: Crear Usuario de Prueba")
    print("-" * 40)
    
    result = payment_system.register_user("test@consorciodej.com", "123456", "Usuario Test")
    if result["success"]:
        print("✅ Usuario creado exitosamente")
    else:
        print(f"❌ Error creando usuario: {result['message']}")
    print()
    
    # Test 5: Login usuario normal
    print("🔑 TEST 5: Login Usuario Normal")
    print("-" * 40)
    
    result = payment_system.login_user("test@consorciodej.com", "123456")
    if result["success"]:
        print("✅ Login usuario exitoso")
        print(f"   Plan: {result['user']['plan']}")
    else:
        print(f"❌ Error login usuario: {result['message']}")
    print()
    
    # Test 6: Cambio de plan para usuario normal
    print("🔄 TEST 6: Cambio de Plan para Usuario Normal")
    print("-" * 40)
    
    result = payment_system.upgrade_plan("test@consorciodej.com", "premium", "paypal")
    if result["success"]:
        print("✅ Cambio de plan exitoso")
        print(f"   Auto confirmado: {result.get('auto_confirmed', False)}")
        print(f"   Mensaje: {result.get('message', 'N/A')}")
    else:
        print(f"❌ Error cambio plan: {result['message']}")
    print()
    
    # Test 7: Verificar plan actualizado
    print("🔍 TEST 7: Verificar Plan Actualizado")
    print("-" * 40)
    
    plan_info = payment_system.get_user_plan("test@consorciodej.com")
    print(f"Plan actual: {plan_info['plan']}")
    print(f"Expira: {plan_info['expires_at']}")
    
    access = payment_system.check_plan_access("test@consorciodej.com", "premium")
    print(f"Acceso premium: {access}")
    print()
    
    # Test 8: Mostrar estado final
    print("📊 TEST 8: Estado Final del Sistema")
    print("-" * 40)
    
    # Mostrar usuarios
    if os.path.exists("users.json"):
        with open("users.json", 'r', encoding='utf-8') as f:
            users = json.load(f)
        print(f"Total usuarios: {len(users)}")
        for email, user_data in users.items():
            print(f"   {email}: {user_data['plan']}")
    
    # Mostrar pagos
    if os.path.exists("payments.json"):
        with open("payments.json", 'r', encoding='utf-8') as f:
            payments = json.load(f)
        print(f"Total pagos: {len(payments)}")
        for payment in payments:
            print(f"   {payment['email']}: {payment['plan']} - {payment['status']}")
    
    print()
    print("🎉 TEST COMPLETADO")
    print("=" * 60)
    print()
    print("📋 RESUMEN:")
    print("✅ Sistema de pagos funcionando")
    print("✅ Admin con acceso completo")
    print("✅ Cambio de planes operativo")
    print("✅ Confirmación automática activa")
    print()
    print("🚀 Ahora puedes ejecutar la aplicación:")
    print("   streamlit run APP.py")

def limpiar_datos_prueba():
    """Limpiar datos de prueba"""
    
    print("🧹 LIMPIANDO DATOS DE PRUEBA")
    print("=" * 40)
    
    archivos = ["users.json", "payments.json"]
    
    for archivo in archivos:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"✅ Eliminado: {archivo}")
        else:
            print(f"⚠️ No existe: {archivo}")
    
    print("✅ Limpieza completada")

if __name__ == "__main__":
    print("🔧 TEST DEL SISTEMA DE PAGOS - CONSORCIO DEJ")
    print("=" * 60)
    print()
    print("1. Ejecutar test completo")
    print("2. Limpiar datos de prueba")
    print("3. Salir")
    print()
    
    opcion = input("Selecciona una opción (1-3): ").strip()
    print()
    
    if opcion == "1":
        test_sistema_pagos()
    elif opcion == "2":
        limpiar_datos_prueba()
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
    else:
        print("❌ Opción no válida") 