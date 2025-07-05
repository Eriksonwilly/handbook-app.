import streamlit as st
import stripe
import json
import sqlite3
from datetime import datetime, timedelta
import hashlib
import os

# Configuración de Stripe (reemplaza con tus claves reales)
STRIPE_PUBLISHABLE_KEY = "pk_test_..."  # Tu clave pública de Stripe
STRIPE_SECRET_KEY = "sk_test_..."       # Tu clave secreta de Stripe

# Configurar Stripe
stripe.api_key = STRIPE_SECRET_KEY

class PaymentSystem:
    def __init__(self):
        self.plans = {
            "gratuito": {
                "name": "Plan Gratuito",
                "price": 0,
                "features": [
                    "✅ Cálculos básicos de estabilidad",
                    "✅ Resultados simples",
                    "✅ Gráficos básicos",
                    "❌ Sin reportes PDF",
                    "❌ Sin análisis completo",
                    "❌ Sin diseño del fuste"
                ],
                "stripe_price_id": None
            },
            "premium": {
                "name": "Plan Premium",
                "price": 9.99,
                "features": [
                    "✅ Cálculos básicos de estabilidad",
                    "✅ Análisis completo con teoría de Rankine",
                    "✅ Diseño y verificación del fuste",
                    "✅ Reportes PDF profesionales",
                    "✅ Gráficos interactivos avanzados",
                    "✅ Verificaciones de estabilidad completas",
                    "✅ Soporte por email"
                ],
                "stripe_price_id": "price_..."  # Tu ID de precio de Stripe
            },
            "empresarial": {
                "name": "Plan Empresarial",
                "price": 29.99,
                "features": [
                    "✅ Todo del Plan Premium",
                    "✅ Múltiples usuarios (hasta 10)",
                    "✅ Reportes personalizados",
                    "✅ API access",
                    "✅ Soporte técnico prioritario",
                    "✅ Capacitación incluida",
                    "✅ Actualizaciones premium"
                ],
                "stripe_price_id": "price_..."  # Tu ID de precio de Stripe
            }
        }
        self.init_database()
    
    def init_database(self):
        """Inicializar base de datos para usuarios y suscripciones"""
        conn = sqlite3.connect('consorcio_dej.db')
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                plan TEXT DEFAULT 'gratuito',
                subscription_id TEXT,
                subscription_status TEXT DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP
            )
        ''')
        
        # Tabla de pagos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                plan TEXT NOT NULL,
                amount REAL NOT NULL,
                stripe_payment_id TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hashear contraseña de forma segura"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, email, password):
        """Registrar nuevo usuario"""
        try:
            conn = sqlite3.connect('consorcio_dej.db')
            cursor = conn.cursor()
            
            password_hash = self.hash_password(password)
            
            cursor.execute('''
                INSERT INTO users (username, email, password_hash, plan)
                VALUES (?, ?, ?, 'gratuito')
            ''', (username, email, password_hash))
            
            conn.commit()
            conn.close()
            return True, "Usuario registrado exitosamente"
        except sqlite3.IntegrityError:
            return False, "El usuario o email ya existe"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def authenticate_user(self, username, password):
        """Autenticar usuario"""
        try:
            conn = sqlite3.connect('consorcio_dej.db')
            cursor = conn.cursor()
            
            password_hash = self.hash_password(password)
            
            cursor.execute('''
                SELECT id, username, email, plan, subscription_status, expires_at
                FROM users 
                WHERE username = ? AND password_hash = ?
            ''', (username, password_hash))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return True, {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'plan': user[3],
                    'status': user[4],
                    'expires_at': user[5]
                }
            else:
                return False, "Usuario o contraseña incorrectos"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def update_user_plan(self, user_id, plan, subscription_id=None):
        """Actualizar plan del usuario"""
        try:
            conn = sqlite3.connect('consorcio_dej.db')
            cursor = conn.cursor()
            
            if plan == "gratuito":
                expires_at = None
            else:
                expires_at = datetime.now() + timedelta(days=30)
            
            cursor.execute('''
                UPDATE users 
                SET plan = ?, subscription_id = ?, expires_at = ?
                WHERE id = ?
            ''', (plan, subscription_id, expires_at, user_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False
    
    def create_checkout_session(self, plan, user_email):
        """Crear sesión de checkout de Stripe"""
        try:
            if plan == "gratuito":
                return None, "Plan gratuito no requiere pago"
            
            plan_data = self.plans[plan]
            if not plan_data["stripe_price_id"]:
                return None, "Plan no configurado para pagos"
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': plan_data["stripe_price_id"],
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='https://tu-app-streamlit.com/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='https://tu-app-streamlit.com/cancel',
                customer_email=user_email,
                metadata={
                    'plan': plan,
                    'user_email': user_email
                }
            )
            
            return checkout_session.url, None
        except Exception as e:
            return None, f"Error creando sesión de pago: {str(e)}"
    
    def show_pricing_page(self):
        """Mostrar página de precios"""
        st.title("💰 Planes y Precios - CONSORCIO DEJ")
        st.markdown("---")
        
        # Crear columnas para los planes
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 20px; border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
                <h2>🆓 Plan Gratuito</h2>
                <h1 style="color: #28a745;">$0</h1>
                <p style="color: #666;">Para siempre</p>
                <ul style="text-align: left;">
                    <li>✅ Cálculos básicos</li>
                    <li>✅ Resultados simples</li>
                    <li>✅ Gráficos básicos</li>
                    <li>❌ Sin reportes PDF</li>
                    <li>❌ Sin análisis completo</li>
                </ul>
                <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                    Empezar Gratis
                </button>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 20px; border: 2px solid #007bff; border-radius: 10px; background-color: #f8f9fa;">
                <h2>⭐ Plan Premium</h2>
                <h1 style="color: #007bff;">$9.99</h1>
                <p style="color: #666;">por mes</p>
                <ul style="text-align: left;">
                    <li>✅ Análisis completo</li>
                    <li>✅ Reportes PDF</li>
                    <li>✅ Diseño del fuste</li>
                    <li>✅ Gráficos avanzados</li>
                    <li>✅ Soporte por email</li>
                </ul>
                <button style="background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                    Suscribirse
                </button>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 20px; border: 2px solid #ffc107; border-radius: 10px; background-color: #fff3cd;">
                <h2>🏢 Plan Empresarial</h2>
                <h1 style="color: #ffc107;">$29.99</h1>
                <p style="color: #666;">por mes</p>
                <ul style="text-align: left;">
                    <li>✅ Múltiples usuarios</li>
                    <li>✅ API access</li>
                    <li>✅ Soporte prioritario</li>
                    <li>✅ Reportes personalizados</li>
                    <li>✅ Capacitación incluida</li>
                </ul>
                <button style="background-color: #ffc107; color: black; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                    Contactar
                </button>
            </div>
            """, unsafe_allow_html=True)
        
        # Comparación de planes
        st.markdown("---")
        st.subheader("📊 Comparación de Planes")
        
        comparison_data = {
            "Característica": [
                "Cálculos básicos",
                "Análisis completo",
                "Diseño del fuste",
                "Reportes PDF",
                "Gráficos avanzados",
                "Soporte técnico",
                "Múltiples usuarios",
                "API access"
            ],
            "Gratuito": ["✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Premium": ["✅", "✅", "✅", "✅", "✅", "✅", "❌", "❌"],
            "Empresarial": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"]
        }
        
        import pandas as pd
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Botones de acción
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🆓 Empezar Gratis", use_container_width=True):
                st.session_state['selected_plan'] = 'gratuito'
                st.session_state['show_payment'] = True
        
        with col2:
            if st.button("⭐ Suscribirse Premium", use_container_width=True):
                st.session_state['selected_plan'] = 'premium'
                st.session_state['show_payment'] = True
        
        with col3:
            if st.button("🏢 Contactar Empresarial", use_container_width=True):
                st.session_state['selected_plan'] = 'empresarial'
                st.session_state['show_payment'] = True
    
    def show_payment_form(self, plan):
        """Mostrar formulario de pago"""
        if plan == "gratuito":
            st.success("🎉 ¡Plan gratuito activado! Ya puedes usar la aplicación.")
            return
        
        st.title(f"💳 Pago - {self.plans[plan]['name']}")
        st.markdown(f"**Precio:** ${self.plans[plan]['price']}/mes")
        
        # Formulario de pago
        with st.form("payment_form"):
            st.subheader("Información de Pago")
            
            email = st.text_input("Email", value=st.session_state.get('user_email', ''))
            card_number = st.text_input("Número de tarjeta", placeholder="1234 5678 9012 3456")
            col1, col2 = st.columns(2)
            with col1:
                exp_month = st.selectbox("Mes", range(1, 13))
            with col2:
                exp_year = st.selectbox("Año", range(2024, 2035))
            cvc = st.text_input("CVC", placeholder="123")
            
            # Términos y condiciones
            agree_terms = st.checkbox("Acepto los términos y condiciones")
            
            submitted = st.form_submit_button("💳 Pagar Ahora")
            
            if submitted:
                if not all([email, card_number, cvc, agree_terms]):
                    st.error("Por favor completa todos los campos")
                else:
                    # Aquí iría la integración real con Stripe
                    st.success("✅ Pago procesado exitosamente!")
                    st.session_state['user_plan'] = plan
                    st.session_state['show_payment'] = False
                    st.rerun()
    
    def check_user_access(self, user_id, required_plan):
        """Verificar si el usuario tiene acceso a una función"""
        try:
            conn = sqlite3.connect('consorcio_dej.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT plan, subscription_status, expires_at
                FROM users 
                WHERE id = ?
            ''', (user_id,))
            
            user_data = cursor.fetchone()
            conn.close()
            
            if not user_data:
                return False
            
            plan, status, expires_at = user_data
            
            # Verificar si la suscripción está activa
            if plan != "gratuito" and expires_at:
                if datetime.now() > datetime.fromisoformat(expires_at):
                    return False
            
            # Verificar nivel de plan
            plan_levels = {"gratuito": 0, "premium": 1, "empresarial": 2}
            required_level = plan_levels.get(required_plan, 0)
            user_level = plan_levels.get(plan, 0)
            
            return user_level >= required_level
            
        except Exception as e:
            st.error(f"Error verificando acceso: {str(e)}")
            return False

# Instanciar sistema de pagos
payment_system = PaymentSystem() 