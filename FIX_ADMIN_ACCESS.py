#!/usr/bin/env python3
"""
Fix Admin Access - CONSORCIO DEJ
Script para arreglar acceso de admin inmediatamente
"""

import json
import os
import hashlib
import datetime

def fix_admin_access():
    """Arreglar acceso de admin inmediatamente"""
    
    print("🔧 ARREGLANDO ACCESO DE ADMIN...")
    print("=" * 50)
    
    # Crear o actualizar usuario admin
    admin_data = {
        "email": "admin@consorciodej.com",
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "name": "admin",
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
            print("✅ Archivo de usuarios cargado")
        except:
            print("⚠️ Error al leer usuarios, creando nuevo archivo")
    
    # Agregar/actualizar admin
    users[admin_data["email"]] = admin_data
    
    # Guardar
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        print("✅ Usuario admin configurado correctamente")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return
    
    print()
    print("🔑 CREDENCIALES DE ADMIN:")
    print("-" * 30)
    print("Usuario: admin")
    print("Contraseña: admin123")
    print("Email: admin@consorciodej.com")
    print("Plan: Empresarial (sin expiración)")
    print()
    
    print("✅ ACCESO COMPLETO HABILITADO")
    print("=" * 50)
    print("Ahora puedes:")
    print("• Acceder al análisis completo")
    print("• Generar reportes detallados")
    print("• Usar todas las funciones premium")
    print("• Gestionar usuarios y pagos")
    print()
    
    print("🚀 Para probar:")
    print("1. Ejecuta: python -m streamlit run APP.py")
    print("2. Inicia sesión con: admin / admin123")
    print("3. Ve a 'Análisis Completo'")
    print("4. ¡Disfruta del acceso completo!")

if __name__ == "__main__":
    fix_admin_access() 