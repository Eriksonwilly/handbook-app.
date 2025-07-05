#!/usr/bin/env python3
"""
Script para configurar Stripe automáticamente
CONSORCIO DEJ - Configuración de Pagos
"""

import stripe
import os
import webbrowser

def setup_stripe():
    """Configurar Stripe para CONSORCIO DEJ"""
    print("💳 Configurando Stripe para CONSORCIO DEJ")
    print("=" * 50)
    
    # Solicitar claves de Stripe
    print("\n📋 Ingresa tus claves de Stripe:")
    print("(Puedes encontrarlas en https://dashboard.stripe.com/apikeys)")
    
    publishable_key = input("Clave pública (pk_test_...): ").strip()
    secret_key = input("Clave secreta (sk_test_...): ").strip()
    
    if not publishable_key or not secret_key:
        print("❌ Las claves son requeridas")
        return
    
    # Configurar Stripe
    stripe.api_key = secret_key
    
    try:
        # Verificar que las claves funcionan
        print("\n🔍 Verificando claves...")
        account = stripe.Account.retrieve()
        print(f"✅ Cuenta verificada: {account.business_profile.name or 'Sin nombre'}")
        
        # Crear productos
        print("\n🏗️ Creando productos...")
        
        # Producto Premium
        premium_product = stripe.Product.create(
            name="CONSORCIO DEJ Premium",
            description="Plan Premium para análisis completo de muros de contención",
            metadata={
                'plan_type': 'premium',
                'features': 'analisis_completo,reportes_pdf,diseño_fuste'
            }
        )
        
        premium_price = stripe.Price.create(
            product=premium_product.id,
            unit_amount=999,  # $9.99 en centavos
            currency='usd',
            recurring={'interval': 'month'},
            metadata={'plan_type': 'premium'}
        )
        
        print(f"✅ Producto Premium creado: {premium_product.id}")
        print(f"✅ Precio Premium creado: {premium_price.id}")
        
        # Producto Empresarial
        empresarial_product = stripe.Product.create(
            name="CONSORCIO DEJ Empresarial",
            description="Plan Empresarial con múltiples usuarios y API access",
            metadata={
                'plan_type': 'empresarial',
                'features': 'multiples_usuarios,api_access,soporte_prioritario'
            }
        )
        
        empresarial_price = stripe.Price.create(
            product=empresarial_product.id,
            unit_amount=2999,  # $29.99 en centavos
            currency='usd',
            recurring={'interval': 'month'},
            metadata={'plan_type': 'empresarial'}
        )
        
        print(f"✅ Producto Empresarial creado: {empresarial_product.id}")
        print(f"✅ Precio Empresarial creado: {empresarial_price.id}")
        
        # Actualizar archivo de configuración
        update_config_file(publishable_key, secret_key, premium_price.id, empresarial_price.id)
        
        print("\n🎉 ¡Configuración completada!")
        print("\n📋 Resumen de configuración:")
        print(f"   Clave pública: {publishable_key}")
        print(f"   Clave secreta: {secret_key}")
        print(f"   Precio Premium: {premium_price.id}")
        print(f"   Precio Empresarial: {empresarial_price.id}")
        
        # Abrir dashboard de Stripe
        print("\n🌐 Abriendo dashboard de Stripe...")
        webbrowser.open("https://dashboard.stripe.com")
        
        print("\n📱 Próximos pasos:")
        print("   1. Configurar webhooks en Stripe")
        print("   2. Probar pagos con tarjetas de prueba")
        print("   3. Activar modo producción cuando estés listo")
        
    except stripe.error.AuthenticationError:
        print("❌ Error de autenticación. Verifica tus claves de Stripe.")
    except stripe.error.StripeError as e:
        print(f"❌ Error de Stripe: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def update_config_file(publishable_key, secret_key, premium_price_id, empresarial_price_id):
    """Actualizar archivo de configuración"""
    config_content = f'''# Configuración de Stripe para CONSORCIO DEJ
# Configurado automáticamente el {os.popen('date').read().strip()}

# Claves de prueba (para desarrollo)
STRIPE_PUBLISHABLE_KEY_TEST = "{publishable_key}"
STRIPE_SECRET_KEY_TEST = "{secret_key}"

# Claves de producción (para cuando publiques)
STRIPE_PUBLISHABLE_KEY_LIVE = "pk_live_..."  # Actualizar cuando estés en producción
STRIPE_SECRET_KEY_LIVE = "sk_live_..."       # Actualizar cuando estés en producción

# IDs de precios de Stripe (creados automáticamente)
STRIPE_PRICE_IDS = {{
    "premium": "{premium_price_id}",
    "empresarial": "{empresarial_price_id}"
}}

# Configuración de webhooks
WEBHOOK_SECRET = "whsec_..."     # Configurar en dashboard de Stripe

# URLs de redirección
SUCCESS_URL = "https://tu-app-streamlit.com/success"
CANCEL_URL = "https://tu-app-streamlit.com/cancel"

# Configuración actualizada automáticamente
'''
    
    with open('stripe_config.py', 'w') as f:
        f.write(config_content)
    
    print("✅ Archivo de configuración actualizado")

def show_instructions():
    """Mostrar instrucciones de configuración"""
    print("\n📖 INSTRUCCIONES DE CONFIGURACIÓN:")
    print("=" * 50)
    
    steps = [
        ("1️⃣", "Crear cuenta en Stripe", "https://stripe.com"),
        ("2️⃣", "Obtener claves API", "https://dashboard.stripe.com/apikeys"),
        ("3️⃣", "Ejecutar este script", "python setup_stripe.py"),
        ("4️⃣", "Configurar webhooks", "https://dashboard.stripe.com/webhooks"),
        ("5️⃣", "Probar pagos", "Usar tarjetas de prueba"),
        ("6️⃣", "Activar producción", "Cambiar a claves live")
    ]
    
    for emoji, step, url in steps:
        print(f"{emoji} {step}")
        if url.startswith("http"):
            print(f"   🌐 {url}")
        else:
            print(f"   💻 {url}")
        print()

def main():
    """Función principal"""
    print("🏗️ CONSORCIO DEJ - Configuración de Stripe")
    print("=" * 50)
    
    # Mostrar instrucciones
    show_instructions()
    
    # Preguntar si continuar
    response = input("¿Quieres configurar Stripe ahora? (s/n): ")
    if response.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        setup_stripe()
    else:
        print("\n📋 Para configurar Stripe manualmente:")
        print("   1. Ve a https://stripe.com")
        print("   2. Crea una cuenta")
        print("   3. Obtén tus claves API")
        print("   4. Ejecuta: python setup_stripe.py")

if __name__ == "__main__":
    main() 