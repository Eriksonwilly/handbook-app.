#!/usr/bin/env python3
"""
Solución Rápida de Pagos - CONSORCIO DEJ
Script para solucionar problemas de pagos y acceso
"""

import json
import os
import hashlib
import datetime

def crear_usuario_ejemplo():
    """Crear usuario de ejemplo para probar pagos"""
    
    print("🔧 CREANDO USUARIO DE EJEMPLO...")
    print("=" * 50)
    
    # Datos del usuario de ejemplo
    user_data = {
        "email": "usuario@ejemplo.com",
        "password": hashlib.sha256("123456".encode()).hexdigest(),
        "name": "Usuario Ejemplo",
        "plan": "gratuito",
        "created_at": datetime.datetime.now().isoformat(),
        "expires_at": None
    }
    
    # Cargar usuarios existentes o crear nuevo
    users_file = "users.json"
    users = {}
    
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
            print("✅ Archivo de usuarios cargado")
        except:
            print("⚠️ Error al leer usuarios, creando nuevo archivo")
    
    # Agregar usuario de ejemplo
    users[user_data["email"]] = user_data
    
    # Guardar
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        print("✅ Usuario de ejemplo creado exitosamente")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return
    
    print()
    print("🔑 CREDENCIALES DE USUARIO EJEMPLO:")
    print("-" * 40)
    print("Email: usuario@ejemplo.com")
    print("Contraseña: 123456")
    print("Plan: Gratuito")
    print()
    
    print("💰 PARA PROBAR PAGOS:")
    print("-" * 30)
    print("1. Inicia sesión con las credenciales")
    print("2. Ve a 'Planes y Precios'")
    print("3. Selecciona 'Actualizar a Premium'")
    print("4. Elige método de pago (Yape)")
    print("5. Sigue las instrucciones")
    print()

def verificar_sistema_pagos():
    """Verificar que el sistema de pagos funcione"""
    
    print("🔍 VERIFICANDO SISTEMA DE PAGOS...")
    print("=" * 50)
    
    # Verificar archivos necesarios
    files_to_check = [
        "simple_payment_system.py",
        "users.json",
        "payments.json"
    ]
    
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✅ {file} - Existe")
        else:
            print(f"❌ {file} - No existe")
    
    print()
    
    # Verificar usuarios
    users_file = "users.json"
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
            
            print(f"📊 Usuarios registrados: {len(users)}")
            for email, user_data in users.items():
                plan = user_data.get('plan', 'N/A')
                name = user_data.get('name', 'N/A')
                print(f"   • {name} ({email}) - Plan: {plan}")
        except Exception as e:
            print(f"❌ Error al leer usuarios: {e}")
    else:
        print("❌ No hay usuarios registrados")
    
    print()
    
    # Verificar pagos
    payments_file = "payments.json"
    if os.path.exists(payments_file):
        try:
            with open(payments_file, 'r', encoding='utf-8') as f:
                payments = json.load(f)
            
            print(f"💰 Pagos registrados: {len(payments)}")
            for payment in payments:
                status = payment.get('status', 'N/A')
                plan = payment.get('plan', 'N/A')
                amount = payment.get('amount', 'N/A')
                print(f"   • {plan} - ${amount} - {status}")
        except Exception as e:
            print(f"❌ Error al leer pagos: {e}")
    else:
        print("❌ No hay pagos registrados")

def limpiar_datos_prueba():
    """Limpiar datos de prueba"""
    
    print("🧹 LIMPIANDO DATOS DE PRUEBA...")
    print("=" * 50)
    
    confirmacion = input("¿Estás seguro? Esto eliminará usuarios y pagos de prueba (s/n): ").strip().lower()
    
    if confirmacion != 's':
        print("❌ Operación cancelada")
        return
    
    # Mantener solo admin y limpiar pagos
    users_file = "users.json"
    payments_file = "payments.json"
    
    # Limpiar usuarios (mantener solo admin)
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
            
            # Mantener solo admin
            admin_email = "admin@consorciodej.com"
            users_limpios = {}
            
            if admin_email in users:
                users_limpios[admin_email] = users[admin_email]
            
            with open(users_file, 'w', encoding='utf-8') as f:
                json.dump(users_limpios, f, indent=2, ensure_ascii=False)
            
            print("✅ Usuarios de prueba eliminados")
        except Exception as e:
            print(f"❌ Error al limpiar usuarios: {e}")
    
    # Limpiar pagos
    if os.path.exists(payments_file):
        try:
            with open(payments_file, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=2, ensure_ascii=False)
            print("✅ Pagos de prueba eliminados")
        except Exception as e:
            print(f"❌ Error al limpiar pagos: {e}")
    
    print("✅ Limpieza completada")

def mostrar_instrucciones_pago():
    """Mostrar instrucciones de pago"""
    
    print("📋 INSTRUCCIONES DE PAGO - CONSORCIO DEJ")
    print("=" * 60)
    print()
    
    print("💰 PLANES DISPONIBLES:")
    print("-" * 30)
    print("• Premium: $29.99/mes")
    print("• Empresarial: $99.99/mes")
    print()
    
    print("💳 MÉTODOS DE PAGO:")
    print("-" * 25)
    print("📱 Yape (Recomendado)")
    print("   • Más rápido")
    print("   • Sin comisiones")
    print("   • Activación inmediata")
    print()
    print("📱 PLIN")
    print("   • Sin comisiones")
    print("   • Proceso instantáneo")
    print()
    print("🏦 Transferencia Bancaria")
    print("   • A cuenta BCP")
    print("   • Sin comisiones")
    print("   • Proceso seguro")
    print()
    print("💳 PayPal")
    print("   • Sin restricciones geográficas")
    print("   • Disponible en Perú")
    print()
    
    print("📱 PROCESO DE PAGO:")
    print("-" * 25)
    print("1. Registrarse o iniciar sesión")
    print("2. Ir a 'Planes y Precios'")
    print("3. Seleccionar plan deseado")
    print("4. Elegir método de pago")
    print("5. Seguir instrucciones específicas")
    print("6. Enviar comprobante por WhatsApp")
    print("7. Esperar confirmación (2 horas max)")
    print("8. ¡Acceso activado!")
    print()
    
    print("📞 CONTACTO PARA SOPORTE:")
    print("-" * 30)
    print("WhatsApp: +51 999 888 777")
    print("Email: consorciodej@gmail.com")
    print()

if __name__ == "__main__":
    while True:
        print("🔧 SOLUCIÓN RÁPIDA DE PAGOS")
        print("=" * 50)
        print()
        print("1. Crear usuario de ejemplo")
        print("2. Verificar sistema de pagos")
        print("3. Limpiar datos de prueba")
        print("4. Mostrar instrucciones de pago")
        print("5. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        print()
        
        if opcion == "1":
            crear_usuario_ejemplo()
        elif opcion == "2":
            verificar_sistema_pagos()
        elif opcion == "3":
            limpiar_datos_prueba()
        elif opcion == "4":
            mostrar_instrucciones_pago()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        print()
        input("Presiona Enter para continuar...")
        print("\n" * 2) 