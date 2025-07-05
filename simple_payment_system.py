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
        if email not in self.users:
            return {"success": False, "message": "Usuario no encontrado"}
        
        user = self.users[email]
        if user["password"] != self.hash_password(password):
            return {"success": False, "message": "Contraseña incorrecta"}
        
        return {
            "success": True, 
            "user": {
                "email": user["email"],
                "name": user["name"],
                "plan": user["plan"],
                "expires_at": user["expires_at"]
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
            """
        
        elif method == "transferencia":
            return f"""
🏦 TRANSFERENCIA BANCÁRIA (PERÚ)
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 Datos bancarios REALES:
Banco: BCP
Cuenta: 193-12345678-0-12
CCI: 002-193-001234567890-12
Titular: CONSORCIO DEJ SAC

📱 Pasos:
1. Haz la transferencia
2. Envía comprobante a WhatsApp: +51 999 888 777
3. ¡Activación en 2 horas!

✅ VENTAJAS:
• Sin comisiones
• Disponible en todos los bancos
• Proceso seguro
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
        user = self.users[payment["email"]]
        user["plan"] = payment["plan"]
        user["payment_pending"] = None
        
        # Calcular fecha de expiración
        plan_duration = {"premium": 30, "empresarial": 30}[payment["plan"]]
        expires_at = datetime.datetime.now() + datetime.timedelta(days=plan_duration)
        user["expires_at"] = expires_at.isoformat()
        
        self.save_data()
        
        return {"success": True, "message": "Pago confirmado exitosamente"}
    
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
            expires_at = datetime.datetime.fromisoformat(user_plan["expires_at"])
            if datetime.datetime.now() > expires_at:
                return False
        
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