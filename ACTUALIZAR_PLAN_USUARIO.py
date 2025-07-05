#!/usr/bin/env python3
"""
Actualizar Plan de Usuario - CONSORCIO DEJ
Script para actualizar el plan del usuario después del pago
"""

import json
import os
import datetime

def actualizar_plan_usuario(email, nuevo_plan):
    """Actualizar el plan de un usuario específico"""
    
    print(f"🔧 ACTUALIZANDO PLAN DE USUARIO...")
    print("=" * 50)
    print(f"Email: {email}")
    print(f"Nuevo plan: {nuevo_plan}")
    print()
    
    # Cargar usuarios
    users_file = "users.json"
    
    if not os.path.exists(users_file):
        print("❌ No existe archivo de usuarios")
        return False
    
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer usuarios: {e}")
        return False
    
    # Verificar si el usuario existe
    if email not in users:
        print(f"❌ Usuario {email} no encontrado")
        return False
    
    # Actualizar plan
    users[email]["plan"] = nuevo_plan
    
    # Calcular fecha de expiración (30 días para premium/empresarial)
    if nuevo_plan in ["premium", "empresarial"]:
        expires_at = datetime.datetime.now() + datetime.timedelta(days=30)
        users[email]["expires_at"] = expires_at.isoformat()
    else:
        users[email]["expires_at"] = None
    
    # Guardar cambios
    try:
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        print("✅ Plan actualizado exitosamente")
        print(f"   Plan: {nuevo_plan}")
        if users[email]["expires_at"]:
            print(f"   Expira: {users[email]['expires_at']}")
        return True
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return False

def confirmar_pago_manual():
    """Confirmar pago manualmente"""
    
    print("💰 CONFIRMAR PAGO MANUALMENTE")
    print("=" * 50)
    
    # Mostrar pagos pendientes
    payments_file = "payments.json"
    
    if os.path.exists(payments_file):
        try:
            with open(payments_file, 'r', encoding='utf-8') as f:
                payments = json.load(f)
            
            pendientes = [p for p in payments if p["status"] == "pendiente"]
            
            if pendientes:
                print(f"📋 Pagos pendientes: {len(pendientes)}")
                print("-" * 40)
                
                for i, payment in enumerate(pendientes):
                    print(f"{i+1}. ID: {payment['id']}")
                    print(f"   Email: {payment['email']}")
                    print(f"   Plan: {payment['plan']}")
                    print(f"   Monto: ${payment['amount']}")
                    print(f"   Método: {payment['payment_method']}")
                    print(f"   Fecha: {payment['created_at']}")
                    print()
                
                # Seleccionar pago a confirmar
                try:
                    seleccion = int(input("Selecciona el número del pago a confirmar: ")) - 1
                    if 0 <= seleccion < len(pendientes):
                        payment = pendientes[seleccion]
                        
                        confirmacion = input(f"¿Confirmar pago de {payment['email']} por ${payment['amount']}? (s/n): ").strip().lower()
                        
                        if confirmacion == 's':
                            # Actualizar estado del pago
                            payment["status"] = "confirmado"
                            payment["confirmed_at"] = datetime.datetime.now().isoformat()
                            
                            # Actualizar plan del usuario
                            if actualizar_plan_usuario(payment["email"], payment["plan"]):
                                # Guardar pagos actualizados
                                with open(payments_file, 'w', encoding='utf-8') as f:
                                    json.dump(payments, f, indent=2, ensure_ascii=False)
                                print("✅ Pago confirmado y plan actualizado")
                            else:
                                print("❌ Error al actualizar plan")
                        else:
                            print("❌ Confirmación cancelada")
                    else:
                        print("❌ Selección inválida")
                except ValueError:
                    print("❌ Entrada inválida")
            else:
                print("✅ No hay pagos pendientes")
        except Exception as e:
            print(f"❌ Error al leer pagos: {e}")
    else:
        print("❌ No hay archivo de pagos")

def mostrar_usuarios():
    """Mostrar todos los usuarios y sus planes"""
    
    print("📊 USUARIOS REGISTRADOS")
    print("=" * 50)
    
    users_file = "users.json"
    
    if not os.path.exists(users_file):
        print("❌ No hay usuarios registrados")
        return
    
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
        
        print(f"Total de usuarios: {len(users)}")
        print("-" * 50)
        
        for email, user_data in users.items():
            plan = user_data.get('plan', 'N/A')
            name = user_data.get('name', 'N/A')
            expires_at = user_data.get('expires_at', 'Nunca')
            
            print(f"📧 {email}")
            print(f"   Nombre: {name}")
            print(f"   Plan: {plan}")
            print(f"   Expira: {expires_at}")
            print()
            
    except Exception as e:
        print(f"❌ Error al leer usuarios: {e}")

def actualizar_plan_interactivo():
    """Actualizar plan de usuario interactivamente"""
    
    print("🔧 ACTUALIZAR PLAN DE USUARIO")
    print("=" * 50)
    
    email = input("Email del usuario: ").strip()
    if not email:
        print("❌ Email requerido")
        return
    
    print("\nPlanes disponibles:")
    print("1. Gratuito")
    print("2. Premium")
    print("3. Empresarial")
    
    try:
        opcion = int(input("Selecciona el plan (1-3): "))
        planes = ["gratuito", "premium", "empresarial"]
        
        if 1 <= opcion <= 3:
            nuevo_plan = planes[opcion - 1]
            actualizar_plan_usuario(email, nuevo_plan)
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Entrada inválida")

if __name__ == "__main__":
    while True:
        print("🔧 ACTUALIZAR PLANES DE USUARIOS")
        print("=" * 50)
        print()
        print("1. Mostrar usuarios")
        print("2. Actualizar plan de usuario")
        print("3. Confirmar pago manualmente")
        print("4. Salir")
        print()
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        print()
        
        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            actualizar_plan_interactivo()
        elif opcion == "3":
            confirmar_pago_manual()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        print()
        input("Presiona Enter para continuar...")
        print("\n" * 2) 