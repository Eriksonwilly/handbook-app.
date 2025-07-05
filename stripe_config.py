# Configuración de Stripe para CONSORCIO DEJ
# Reemplaza estas claves con las tuyas reales de Stripe

# Claves de prueba (para desarrollo)
STRIPE_PUBLISHABLE_KEY_TEST = "pk_test_..."  # Tu clave pública de prueba
STRIPE_SECRET_KEY_TEST = "sk_test_..."       # Tu clave secreta de prueba

# Claves de producción (para cuando publiques)
STRIPE_PUBLISHABLE_KEY_LIVE = "pk_live_..."  # Tu clave pública de producción
STRIPE_SECRET_KEY_LIVE = "sk_live_..."       # Tu clave secreta de producción

# IDs de precios de Stripe (crear en el dashboard de Stripe)
STRIPE_PRICE_IDS = {
    "premium": "price_...",      # ID del precio para plan premium ($9.99/mes)
    "empresarial": "price_..."   # ID del precio para plan empresarial ($29.99/mes)
}

# Configuración de webhooks
WEBHOOK_SECRET = "whsec_..."     # Secreto del webhook de Stripe

# URLs de redirección
SUCCESS_URL = "https://tu-app-streamlit.com/success"
CANCEL_URL = "https://tu-app-streamlit.com/cancel"

"""
INSTRUCCIONES PARA CONFIGURAR STRIPE:

1. Crear cuenta en Stripe:
   - Ve a https://stripe.com
   - Regístrate como desarrollador
   - Completa la verificación

2. Obtener claves API:
   - Ve a Dashboard > Developers > API keys
   - Copia las claves de prueba y producción

3. Crear productos y precios:
   - Ve a Dashboard > Products
   - Crea producto "CONSORCIO DEJ Premium"
   - Precio: $9.99/mes (recurring)
   - Crea producto "CONSORCIO DEJ Empresarial"
   - Precio: $29.99/mes (recurring)

4. Configurar webhooks:
   - Ve a Dashboard > Developers > Webhooks
   - Endpoint: https://tu-app-streamlit.com/webhook
   - Events: checkout.session.completed, customer.subscription.updated

5. Reemplazar las claves en este archivo

6. Actualizar payment_system.py con las claves reales

NOTA: Usa las claves de prueba durante el desarrollo
""" 