#!/usr/bin/env python3
"""
Verificador de Acceso Administrador - CONSORCIO DEJ
Script para verificar y configurar el acceso de administrador
"""

import json
import os
import hashlib
import datetime

def verificar_admin():
    """Verificar el estado del usuario administrador"""
    
    print("=" * 60)
    print("    VERIFICADOR DE ACCESO ADMINISTRADOR")
    print("=" * 60)
    print()
    
    # Verificar archivo de usuarios
    users_file = "users.json"
    
    if not os.path.exists(users_file):
        print("❌ No existe archivo de usuarios")
        print("✅ Se creará automáticamente al ejecutar la app")
        return
    
    # Cargar usuarios
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except:
        print("❌ Error al leer archivo de usuarios")
        return
    
    # Buscar usuario admin
    admin_email = "admin@consorciodej.com"
    admin_found = False
    
    for email, user_data in users.items():
        if email == admin_email:
            admin_found = True
            print("✅ Usuario administrador encontrado:")
            print(f"   Email: {email}")
            print(f"   Nombre: {user_data.get('name', 'N/A')}")
            print(f"   Plan: {user_data.get('plan', 'N/A')}")
            print(f"   Creado: {user_data.get('created_at', 'N/A')}")
            print(f"   Expira: {user_data.get('expires_at', 'Nunca')}")
            break
    
    if not admin_found:
        print("❌ Usuario administrador no encontrado")
        print("✅ Se creará automáticamente al ejecutar la app")
    
    print()
    print("🔑 CREDENCIALES DE ACCESO:")
    print("-" * 40)
    print("Usuario: admin")
    print("Contraseña: admin123")
    print("Email: admin@consorciodej.com")
    print()
    
    print("🎯 PLANES DISPONIBLES:")
    print("-" * 40)
    print("• Gratuito: Acceso básico")
    print("• Premium: $29.99/mes - Análisis completo")
    print("• Empresarial: $99.99/mes - Todo incluido")
    print()
    
    print("🚀 CÓMO ACCEDER AL MODO EMPRESARIAL:")
    print("-" * 40)
    print("1. Inicia sesión con: admin / admin123")
    print("2. Ve a 'Configuración' → 'Cambiar Plan'")
    print("3. Selecciona 'Empresarial'")
    print("4. Elige método de pago")
    print("5. ¡Listo! Acceso completo")
    print()

def crear_admin_manual():
    """Crear usuario admin manualmente"""
    
    print("🔧 CREAR USUARIO ADMIN MANUALMENTE")
    print("-" * 40)
    
    # Datos del admin
    admin_data = {
        "email": "admin@consorciodej.com",
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "name": "Administrador",
        "plan": "empresarial",
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
        except:
            print("⚠️ Error al leer usuarios existentes, creando nuevo archivo")
    
    # Agregar admin
    users[admin_data["email"]] = admin_data
    
    # Guardar
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        print("✅ Usuario admin creado exitosamente")
        print("   Email: admin@consorciodej.com")
        print("   Contraseña: admin123")
        print("   Plan: Empresarial")
    except Exception as e:
        print(f"❌ Error al crear admin: {e}")

def mostrar_usuarios():
    """Mostrar todos los usuarios registrados"""
    
    users_file = "users.json"
    
    if not os.path.exists(users_file):
        print("❌ No hay usuarios registrados")
        return
    
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except:
        print("❌ Error al leer usuarios")
        return
    
    print("📋 USUARIOS REGISTRADOS:")
    print("-" * 60)
    print(f"{'Email':<30} {'Nombre':<20} {'Plan':<12} {'Estado'}")
    print("-" * 60)
    
    for email, user_data in users.items():
        plan = user_data.get('plan', 'N/A')
        name = user_data.get('name', 'N/A')
        
        # Verificar si el plan ha expirado
        expires_at = user_data.get('expires_at')
        if expires_at:
            try:
                expires_date = datetime.datetime.fromisoformat(expires_at)
                if datetime.datetime.now() > expires_date:
                    status = "❌ Expirado"
                else:
                    status = "✅ Activo"
            except:
                status = "❓ Error"
        else:
            status = "✅ Sin expiración"
        
        print(f"{email:<30} {name:<20} {plan:<12} {status}")
    
    print()

def limpiar_usuarios():
    """Limpiar usuarios de prueba"""
    
    print("🧹 LIMPIAR USUARIOS DE PRUEBA")
    print("-" * 40)
    
    confirmacion = input("¿Estás seguro? Esto eliminará usuarios de prueba (s/n): ").strip().lower()
    
    if confirmacion != 's':
        print("❌ Operación cancelada")
        return
    
    users_file = "users.json"
    
    if not os.path.exists(users_file):
        print("❌ No hay usuarios para limpiar")
        return
    
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except:
        print("❌ Error al leer usuarios")
        return
    
    # Mantener solo el admin
    admin_email = "admin@consorciodej.com"
    users_limpios = {}
    
    if admin_email in users:
        users_limpios[admin_email] = users[admin_email]
    
    # Guardar usuarios limpios
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users_limpios, f, indent=2, ensure_ascii=False)
        print("✅ Usuarios de prueba eliminados")
        print("✅ Solo se mantiene el usuario admin")
    except Exception as e:
        print(f"❌ Error al limpiar: {e}")

if __name__ == "__main__":
    while True:
        print("🔧 VERIFICADOR DE ACCESO ADMINISTRADOR")
        print("=" * 50)
        print()
        print("1. Verificar estado del admin")
        print("2. Crear admin manualmente")
        print("3. Mostrar todos los usuarios")
        print("4. Limpiar usuarios de prueba")
        print("5. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        print()
        
        if opcion == "1":
            verificar_admin()
        elif opcion == "2":
            crear_admin_manual()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            limpiar_usuarios()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        print()
        input("Presiona Enter para continuar...")
        print("\n" * 2) 