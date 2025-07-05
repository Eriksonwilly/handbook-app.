#!/usr/bin/env python3
"""
SOLUCIÓN RÁPIDA - SISTEMA DE PAGOS
CONSORCIO DEJ - Muros de Contención
"""

import json
import os
import datetime

def solucion_rapida_pagos():
    """Solución rápida para activar el sistema de pagos"""
    
    print("🚀 SOLUCIÓN RÁPIDA - SISTEMA DE PAGOS")
    print("=" * 60)
    print()
    
    # Crear archivo de usuarios con admin
    users = {
        "admin": {
            "email": "admin",
            "password": "admin123",
            "name": "Administrador",
            "plan": "empresarial",
            "created_at": datetime.datetime.now().isoformat(),
            "expires_at": None
        },
        "admin@consorciodej.com": {
            "email": "admin@consorciodej.com",
            "password": "admin123",
            "name": "Administrador",
            "plan": "empresarial",
            "created_at": datetime.datetime.now().isoformat(),
            "expires_at": None
        }
    }
    
    # Guardar usuarios
    with open("users.json", 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
    
    print("✅ Archivo de usuarios creado")
    print("✅ Admin configurado con plan empresarial")
    print()
    
    # Crear archivo de pagos vacío
    payments = []
    with open("payments.json", 'w', encoding='utf-8') as f:
        json.dump(payments, f, indent=2, ensure_ascii=False)
    
    print("✅ Archivo de pagos creado")
    print()
    
    # Verificar sistema de pagos
    try:
        from simple_payment_system import payment_system
        print("✅ Sistema de pagos funcionando")
        
        # Test de login admin
        result = payment_system.login_user("admin", "admin123")
        if result["success"]:
            print("✅ Login admin exitoso")
            print(f"   Plan: {result['user']['plan']}")
        else:
            print(f"❌ Error login: {result['message']}")
        
        # Test de cambio de plan
        result = payment_system.upgrade_plan("admin", "empresarial", "admin")
        if result["success"]:
            print("✅ Cambio de plan exitoso")
            print(f"   Mensaje: {result['message']}")
        else:
            print(f"❌ Error cambio plan: {result['message']}")
            
    except Exception as e:
        print(f"❌ Error en sistema de pagos: {e}")
        print("⚠️ Verifica que simple_payment_system.py existe")
    
    print()
    print("🎉 SOLUCIÓN APLICADA")
    print("=" * 60)
    print()
    print("🔑 CREDENCIALES DE ADMINISTRADOR:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    print("   Plan: Empresarial (acceso completo)")
    print()
    print("🚀 AHORA PUEDES:")
    print("   1. Ejecutar: streamlit run APP.py")
    print("   2. Iniciar sesión como admin")
    print("   3. Acceder a todas las funciones")
    print("   4. Cambiar plan desde el sidebar")
    print()
    print("✅ El administrador tiene acceso directo sin pagos")

def verificar_sistema():
    """Verificar que el sistema esté funcionando"""
    
    print("🔍 VERIFICANDO SISTEMA")
    print("=" * 40)
    
    archivos = ["simple_payment_system.py", "users.json", "payments.json"]
    
    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - FALTANTE")
    
    print()
    
    # Verificar contenido de usuarios
    if os.path.exists("users.json"):
        with open("users.json", 'r', encoding='utf-8') as f:
            users = json.load(f)
        
        print(f"👥 Usuarios registrados: {len(users)}")
        for email, user_data in users.items():
            print(f"   {email}: {user_data['plan']}")
    
    print()
    print("✅ Verificación completada")

if __name__ == "__main__":
    print("🔧 SOLUCIÓN RÁPIDA - CONSORCIO DEJ")
    print("=" * 50)
    print()
    print("1. Aplicar solución rápida")
    print("2. Verificar sistema")
    print("3. Salir")
    print()
    
    opcion = input("Selecciona una opción (1-3): ").strip()
    print()
    
    if opcion == "1":
        solucion_rapida_pagos()
    elif opcion == "2":
        verificar_sistema()
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
    else:
        print("❌ Opción no válida") 