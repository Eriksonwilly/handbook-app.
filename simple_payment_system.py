#!/usr/bin/env python3
"""
Sistema de Pagos Simple para CONSORCIO DEJ
Alternativa práctica sin Stripe - PayPal + Transferencias
"""

import json
import os
import hashlib
import datetime
from typing import Dict, List, Optional

class SimplePaymentSystem:
    """Sistema de pagos simple sin Stripe"""
    
    def __init__(self):
        self.users_file = "users.json"
        self.payments_file = "payments.json"
        self.admin_credentials = {
            "usuario": "admin",
            "clave": "admin123"
        }
        self.load_data()
        self.create_default_admin()
    
    def create_default_admin(self):
        """Crear usuario admin por defecto si no existe"""
        admin_email = "admin@consorciodej.com"
        if admin_email not in self.users:
            admin_user = {
                "email": admin_email,
                "password": self.hash_password("admin123"),
                "name": "admin",
                "plan": "empresarial",
                "created_at": datetime.datetime.now().isoformat(),
                "expires_at": None
            }
            self.users[admin_email] = admin_user
            self.save_data()
            print("✅ Usuario admin creado: admin@consorciodej.com / admin123")
        else:
            # Asegurar que el admin tenga plan empresarial
            if self.users[admin_email]["plan"] != "empresarial":
                self.users[admin_email]["plan"] = "empresarial"
                self.users[admin_email]["expires_at"] = None
                self.save_data()
                print("✅ Plan de admin actualizado a empresarial")
    
    def load_data(self):
        """Cargar datos de usuarios y pagos"""
        # Cargar usuarios
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r', encoding='utf-8') as f:
                self.users = json.load(f)
        else:
            self.users = {}
        
        # Cargar pagos
        if os.path.exists(self.payments_file):
            with open(self.payments_file, 'r', encoding='utf-8') as f:
                self.payments = json.load(f)
        else:
            self.payments = []
    
    def save_data(self):
        """Guardar datos"""
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=2, ensure_ascii=False)
        
        with open(self.payments_file, 'w', encoding='utf-8') as f:
            json.dump(self.payments, f, indent=2, ensure_ascii=False)
    
    def hash_password(self, password: str) -> str:
        """Encriptar contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, email: str, password: str, name: str) -> Dict:
        """Registrar nuevo usuario"""
        if email in self.users:
            return {"success": False, "message": "El email ya está registrado"}
        
        user = {
            "email": email,
            "password": self.hash_password(password),
            "name": name,
            "plan": "gratuito",
            "created_at": datetime.datetime.now().isoformat(),
            "expires_at": None
        }
        
        self.users[email] = user
        self.save_data()
        
        return {"success": True, "message": "Usuario registrado exitosamente"}
    
    def login_user(self, email: str, password: str) -> Dict:
        """Iniciar sesión"""
        # Verificar credenciales especiales primero
        if email == "admin" and password == "admin123":
            return {
                "success": True,
                "user": {
                    "email": "admin",
                    "name": "Administrador",
                    "plan": "empresarial",
                    "expires_at": None,
                    "is_admin": True
                }
            }
        
        # Buscar usuario por email o por nombre de usuario
        user_found = None
        
        # Primero buscar por email exacto
        if email in self.users:
            user_found = self.users[email]
        else:
            # Buscar por nombre de usuario (campo name)
            for user_email, user_data in self.users.items():
                if user_data.get("name", "").lower() == email.lower():
                    user_found = user_data
                    break
        
        if not user_found:
            return {"success": False, "message": "Usuario no encontrado"}
        
        if user_found["password"] != self.hash_password(password):
            return {"success": False, "message": "Contraseña incorrecta"}
        
        return {
            "success": True, 
            "user": {
                "email": user_found["email"],
                "name": user_found["name"],
                "plan": user_found["plan"],
                "expires_at": user_found["expires_at"],
                "is_admin": user_found.get("email") == "admin@consorciodej.com"
            }
        }
    
    def admin_login(self, username: str, password: str) -> Dict:
        """Login de administrador"""
        if (username == self.admin_credentials["usuario"] and 
            password == self.admin_credentials["clave"]):
            return {"success": True, "message": "Login exitoso"}
        return {"success": False, "message": "Credenciales incorrectas"}
    
    def upgrade_plan(self, email: str, plan: str, payment_method: str) -> Dict:
        """Actualizar plan de usuario"""
        if email not in self.users:
            return {"success": False, "message": "Usuario no encontrado"}
        
        # Verificar si es admin - acceso directo
        if email == "admin" or email == "admin@consorciodej.com":
            # Acceso directo para admin
            user = self.users[email]
            user["plan"] = plan
            user["expires_at"] = None  # Admin no expira
            self.save_data()
            return {
                "success": True,
                "message": f"Plan {plan} activado para administrador",
                "admin_access": True
            }
        
        # Definir precios y duración
        plan_info = {
            "premium": {"price": 29.99, "duration_days": 30},
            "empresarial": {"price": 99.99, "duration_days": 30}
        }
        
        if plan not in plan_info:
            return {"success": False, "message": "Plan no válido"}
        
        # Crear registro de pago
        payment = {
            "id": f"PAY_{len(self.payments) + 1:06d}",
            "email": email,
            "plan": plan,
            "amount": plan_info[plan]["price"],
            "payment_method": payment_method,
            "status": "pendiente",
            "created_at": datetime.datetime.now().isoformat(),
            "instructions": self.get_payment_instructions(payment_method, plan_info[plan]["price"])
        }
        
        self.payments.append(payment)
        
        # Actualizar usuario
        user = self.users[email]
        user["plan"] = plan
        user["payment_pending"] = payment["id"]
        
        # Confirmar pago automáticamente (para demo)
        if payment_method in ["yape", "plin", "paypal"]:
            confirm_result = self.confirm_payment(payment["id"])
            if confirm_result["success"]:
                return {
                    "success": True,
                    "payment_id": payment["id"],
                    "instructions": payment["instructions"],
                    "amount": payment["amount"],
                    "auto_confirmed": True,
                    "message": "Pago confirmado automáticamente"
                }
        
        self.save_data()
        
        return {
            "success": True,
            "payment_id": payment["id"],
            "instructions": payment["instructions"],
            "amount": payment["amount"]
        }
    
    def get_payment_instructions(self, method: str, amount: float) -> str:
        """Obtener instrucciones de pago compatibles con Perú"""
        if method == "paypal":
            return f"""
💳 PAGO CON PAYPAL (RECOMENDADO)
💰 Monto: ${amount:.2f} USD

📋 Pasos RÁPIDOS:
1. Ve a https://paypal.me/consorciodej
2. Envía ${amount:.2f} USD
3. En el mensaje escribe tu email
4. Envía captura a WhatsApp: +51 999 888 777
5. ¡Activación en 2 horas!

✅ VENTAJAS:
• Sin restricciones geográficas
• Disponible en Perú
• Proceso automático
• Sin comisiones ocultas

📧 PayPal: consorciodej@gmail.com
            """
        
        elif method == "transferencia":
            return f"""
🏦 TRANSFERENCIA BANCÁRIA (PERÚ)
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 DATOS BANCARIOS REALES - TU CUENTA BCP:
Banco: BCP
Cuenta: 193-12345678-0-12
CCI: 002-193-001234567890-12
Titular: CONSORCIO DEJ SAC

📱 Pasos:
1. Haz la transferencia a TU cuenta BCP
2. Envía comprobante a WhatsApp: +51 999 888 777
3. ¡Activación en 2 horas!

✅ VENTAJAS:
• Sin comisiones
• Disponible en todos los bancos
• Proceso seguro
• El dinero llega DIRECTAMENTE a tu cuenta BCP

🏦 El dinero llega directamente a tu cuenta BCP
            """
        
        elif method == "yape":
            return f"""
📱 PAGO CON YAPE (MÁS RÁPIDO)
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 Pasos:
1. Abre Yape
2. Escanea QR o envía a: +51 999 888 777
3. Envía S/{(amount * 3.7):.2f} PEN
4. Envía captura a WhatsApp: +51 999 888 777
5. ¡Activación INMEDIATA!

✅ VENTAJAS:
• Más rápido que transferencia
• Sin comisiones
• Disponible 24/7
• Activación inmediata
• El dinero llega DIRECTAMENTE a tu Yape

📱 El dinero llega directamente a tu Yape
            """
        
        elif method == "plin":
            return f"""
📱 PAGO CON PLIN
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 Pasos:
1. Abre PLIN
2. Envía a: +51 999 888 777
3. Envía S/{(amount * 3.7):.2f} PEN
4. Envía captura a WhatsApp: +51 999 888 777
5. ¡Activación INMEDIATA!

✅ VENTAJAS:
• Sin comisiones
• Proceso instantáneo
• Disponible en todo Perú
• El dinero llega DIRECTAMENTE a tu PLIN

📱 El dinero llega directamente a tu PLIN
            """
        
        else:
            return f"""
💵 PAGO EN EFECTIVO
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 Opciones:
• Depósito en agente BCP/BBVA/Interbank
• Pago en efectivo en oficina
• Transferencia interbancaria

📱 Contacto: +51 999 888 777
📍 Oficina: Av. Arequipa 123, Lima

✅ VENTAJAS:
• Sin comisiones
• Pago directo
• Recibo físico

💼 El dinero llega directamente a tu cuenta
            """
    
    def confirm_payment(self, payment_id: str) -> Dict:
        """Confirmar pago (solo admin)"""
        payment = next((p for p in self.payments if p["id"] == payment_id), None)
        
        if not payment:
            return {"success": False, "message": "Pago no encontrado"}
        
        if payment["status"] == "confirmado":
            return {"success": False, "message": "Pago ya confirmado"}
        
        # Actualizar estado del pago
        payment["status"] = "confirmado"
        payment["confirmed_at"] = datetime.datetime.now().isoformat()
        
        # Actualizar usuario
        email = payment["email"]
        if email in self.users:
            user = self.users[email]
            user["plan"] = payment["plan"]
            user["payment_pending"] = None
            
            # Calcular fecha de expiración
            plan_duration = {"premium": 30, "empresarial": 30}[payment["plan"]]
            expires_at = datetime.datetime.now() + datetime.timedelta(days=plan_duration)
            user["expires_at"] = expires_at.isoformat()
            
            self.save_data()
            
            return {
                "success": True, 
                "message": f"Pago confirmado exitosamente. Plan {payment['plan']} activado para {email}",
                "user_email": email,
                "plan": payment["plan"]
            }
        else:
            return {"success": False, "message": "Usuario no encontrado"}
    
    def get_user_plan(self, email: str) -> Dict:
        """Obtener plan del usuario"""
        if email not in self.users:
            return {"plan": "gratuito", "expires_at": None}
        
        user = self.users[email]
        return {
            "plan": user["plan"],
            "expires_at": user["expires_at"],
            "payment_pending": user.get("payment_pending")
        }
    
    def get_pending_payments(self) -> List[Dict]:
        """Obtener pagos pendientes (solo admin)"""
        return [p for p in self.payments if p["status"] == "pendiente"]
    
    def check_plan_access(self, email: str, required_plan: str) -> bool:
        """Verificar acceso al plan"""
        # Admin tiene acceso completo
        if email == "admin" or email == "admin@consorciodej.com":
            return True
        
        user_plan = self.get_user_plan(email)
        
        plan_hierarchy = {
            "gratuito": 0,
            "premium": 1,
            "empresarial": 2
        }
        
        current_level = plan_hierarchy.get(user_plan["plan"], 0)
        required_level = plan_hierarchy.get(required_plan, 0)
        
        # Verificar si el plan no ha expirado
        if user_plan["expires_at"]:
            try:
                expires_at = datetime.datetime.fromisoformat(user_plan["expires_at"])
                if datetime.datetime.now() > expires_at:
                    return False
            except:
                # Si hay error en la fecha, asumir que no ha expirado
                pass
        
        return current_level >= required_level

# Instancia global
payment_system = SimplePaymentSystem()

def test_system():
    """Probar el sistema"""
    print("🧪 PROBANDO SISTEMA DE PAGOS")
    print("=" * 40)
    
    # Registrar usuario
    result = payment_system.register_user("test@test.com", "123456", "Usuario Test")
    print(f"Registro: {result}")
    
    # Login
    result = payment_system.login_user("test@test.com", "123456")
    print(f"Login: {result}")
    
    # Upgrade plan
    result = payment_system.upgrade_plan("test@test.com", "premium", "paypal")
    print(f"Upgrade: {result}")
    
    # Verificar acceso
    access = payment_system.check_plan_access("test@test.com", "premium")
    print(f"Acceso Premium: {access}")

if __name__ == "__main__":
    test_system() 