#!/usr/bin/env python3
"""
Activar Pagos Automáticos - CONSORCIO DEJ
Script para activar pagos automáticamente y actualizar planes
"""

import json
import os
import datetime

def activar_pagos_automaticos():
    """Activar todos los pagos pendientes automáticamente"""
    
    print("💰 ACTIVANDO PAGOS AUTOMÁTICOS...")
    print("=" * 50)
    
    payments_file = "payments.json"
    users_file = "users.json"
    
    if not os.path.exists(payments_file):
        print("❌ No hay archivo de pagos")
        return
    
    try:
        with open(payments_file, 'r', encoding='utf-8') as f:
            payments = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer pagos: {e}")
        return
    
    # Filtrar pagos pendientes
    pendientes = [p for p in payments if p["status"] == "pendiente"]
    
    if not pendientes:
        print("✅ No hay pagos pendientes")
        return
    
    print(f"📋 Pagos pendientes encontrados: {len(pendientes)}")
    print()
    
    # Cargar usuarios
    users = {}
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except Exception as e:
            print(f"❌ Error al leer usuarios: {e}")
            return
    
    # Activar cada pago
    activados = 0
    for payment in pendientes:
        try:
            # Actualizar estado del pago
            payment["status"] = "confirmado"
            payment["confirmed_at"] = datetime.datetime.now().isoformat()
            
            # Actualizar plan del usuario
            email = payment["email"]
            plan = payment["plan"]
            
            if email in users:
                users[email]["plan"] = plan
                
                # Calcular fecha de expiración
                if plan in ["premium", "empresarial"]:
                    expires_at = datetime.datetime.now() + datetime.timedelta(days=30)
                    users[email]["expires_at"] = expires_at.isoformat()
                else:
                    users[email]["expires_at"] = None
                
                print(f"✅ Pago activado: {email} → {plan}")
                activados += 1
            else:
                print(f"⚠️ Usuario no encontrado: {email}")
                
        except Exception as e:
            print(f"❌ Error al activar pago {payment['id']}: {e}")
    
    # Guardar cambios
    try:
        with open(payments_file, 'w', encoding='utf-8') as f:
            json.dump(payments, f, indent=2, ensure_ascii=False)
        
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        
        print()
        print(f"🎉 ACTIVACIÓN COMPLETADA")
        print(f"✅ Pagos activados: {activados}")
        print(f"✅ Usuarios actualizados: {activados}")
        print()
        print("📱 Los usuarios ahora tienen acceso completo a sus planes")
        
    except Exception as e:
        print(f"❌ Error al guardar cambios: {e}")

def mostrar_estado_pagos():
    """Mostrar estado actual de pagos y usuarios"""
    
    print("📊 ESTADO ACTUAL DE PAGOS Y USUARIOS")
    print("=" * 50)
    
    # Mostrar pagos
    payments_file = "payments.json"
    if os.path.exists(payments_file):
        try:
            with open(payments_file, 'r', encoding='utf-8') as f:
                payments = json.load(f)
            
            print(f"💰 Total de pagos: {len(payments)}")
            
            pendientes = [p for p in payments if p["status"] == "pendiente"]
            confirmados = [p for p in payments if p["status"] == "confirmado"]
            
            print(f"   • Pendientes: {len(pendientes)}")
            print(f"   • Confirmados: {len(confirmados)}")
            print()
            
            if pendientes:
                print("📋 PAGOS PENDIENTES:")
                for payment in pendientes:
                    print(f"   • {payment['email']} - {payment['plan']} - ${payment['amount']}")
                print()
                
        except Exception as e:
            print(f"❌ Error al leer pagos: {e}")
    
    # Mostrar usuarios
    users_file = "users.json"
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
            
            print(f"👥 Total de usuarios: {len(users)}")
            
            planes = {}
            for user_data in users.values():
                plan = user_data.get('plan', 'gratuito')
                planes[plan] = planes.get(plan, 0) + 1
            
            for plan, count in planes.items():
                print(f"   • {plan.title()}: {count}")
            print()
            
        except Exception as e:
            print(f"❌ Error al leer usuarios: {e}")

def crear_usuario_premium():
    """Crear usuario con plan premium para pruebas"""
    
    print("🔧 CREANDO USUARIO PREMIUM DE PRUEBA...")
    print("=" * 50)
    
    # Datos del usuario premium
    user_data = {
        "email": "premium@test.com",
        "password": "123456",  # Se hasheará
        "name": "Usuario Premium",
        "plan": "empresarial",
        "created_at": datetime.datetime.now().isoformat(),
        "expires_at": (datetime.datetime.now() + datetime.timedelta(days=30)).isoformat()
    }
    
    # Hashear contraseña
    import hashlib
    user_data["password"] = hashlib.sha256(user_data["password"].encode()).hexdigest()
    
    # Cargar usuarios existentes
    users_file = "users.json"
    users = {}
    
    if os.path.exists(users_file):
        try:
            with open(users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except:
            pass
    
    # Agregar usuario premium
    users[user_data["email"]] = user_data
    
    # Guardar
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        
        print("✅ Usuario premium creado exitosamente")
        print()
        print("🔑 CREDENCIALES:")
        print("   Email: premium@test.com")
        print("   Contraseña: 123456")
        print("   Plan: Empresarial")
        print()
        print("🚀 Ahora puedes probar el acceso completo")
        
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")

if __name__ == "__main__":
    while True:
        print("💰 ACTIVACIÓN AUTOMÁTICA DE PAGOS")
        print("=" * 50)
        print()
        print("1. Activar pagos automáticamente")
        print("2. Mostrar estado actual")
        print("3. Crear usuario premium de prueba")
        print("4. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        print()
        
        if opcion == "1":
            activar_pagos_automaticos()
        elif opcion == "2":
            mostrar_estado_pagos()
        elif opcion == "3":
            crear_usuario_premium()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        print()
        input("Presiona Enter para continuar...")
        print("\n" * 2) 