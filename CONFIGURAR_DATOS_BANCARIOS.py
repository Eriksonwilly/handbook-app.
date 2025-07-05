#!/usr/bin/env python3
"""
Configurador de Datos Bancarios - CONSORCIO DEJ
Script para configurar fácilmente tus datos bancarios reales
"""

import os
import re

def configurar_datos_bancarios():
    """Configurar datos bancarios interactivamente"""
    
    print("=" * 60)
    print("    CONFIGURADOR DE DATOS BANCARIOS - CONSORCIO DEJ")
    print("=" * 60)
    print()
    
    # Solicitar datos bancarios
    print("🏦 CONFIGURAR DATOS BANCARIOS BCP")
    print("-" * 40)
    
    banco = input("Banco (ej: BCP): ").strip() or "BCP"
    cuenta = input("Número de cuenta (ej: 193-87654321-0-12): ").strip()
    cci = input("CCI (ej: 002-193-008765432109-12): ").strip()
    titular = input("Nombre del titular: ").strip()
    
    print()
    print("📱 CONFIGURAR DATOS MÓVILES")
    print("-" * 40)
    
    yape = input("Número Yape (+51 987 654 321): ").strip()
    plin = input("Número PLIN (+51 987 654 321): ").strip()
    whatsapp = input("Número WhatsApp (+51 987 654 321): ").strip()
    
    print()
    print("💳 CONFIGURAR PAYPAL")
    print("-" * 40)
    
    paypal_email = input("Email PayPal: ").strip()
    paypal_link = input("Link PayPal.me: ").strip()
    
    # Validar datos obligatorios
    if not cuenta or not cci or not titular:
        print("❌ ERROR: Los datos bancarios son obligatorios")
        return
    
    if not yape and not plin and not whatsapp:
        print("❌ ERROR: Al menos un método de pago móvil es obligatorio")
        return
    
    # Actualizar archivo simple_payment_system.py
    actualizar_archivo_pagos(banco, cuenta, cci, titular, yape, plin, whatsapp, paypal_email, paypal_link)
    
    print()
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 60)
    print("Los datos bancarios han sido actualizados en el sistema.")
    print("Ahora el dinero llegará directamente a tu cuenta BCP.")
    print()
    print("Para probar:")
    print("1. Ejecuta: python -m streamlit run APP.py")
    print("2. Ve a 'Cambiar Plan' → 'Empresarial'")
    print("3. Selecciona 'Transferencia Bancaria'")
    print("4. Verifica que aparezcan tus datos reales")

def actualizar_archivo_pagos(banco, cuenta, cci, titular, yape, plin, whatsapp, paypal_email, paypal_link):
    """Actualizar el archivo simple_payment_system.py con los nuevos datos"""
    
    archivo = "simple_payment_system.py"
    
    if not os.path.exists(archivo):
        print(f"❌ ERROR: No se encontró el archivo {archivo}")
        return
    
    # Leer el archivo
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Actualizar datos bancarios
    contenido = re.sub(
        r'Banco: BCP',
        f'Banco: {banco}',
        contenido
    )
    
    contenido = re.sub(
        r'Cuenta: 193-12345678-0-12',
        f'Cuenta: {cuenta}',
        contenido
    )
    
    contenido = re.sub(
        r'CCI: 002-193-001234567890-12',
        f'CCI: {cci}',
        contenido
    )
    
    contenido = re.sub(
        r'Titular: CONSORCIO DEJ SAC',
        f'Titular: {titular}',
        contenido
    )
    
    # Actualizar números móviles
    if yape:
        contenido = re.sub(
            r'\+51 999 888 777',
            yape,
            contenido
        )
    
    if plin:
        contenido = re.sub(
            r'\+51 999 888 777',
            plin,
            contenido
        )
    
    if whatsapp:
        contenido = re.sub(
            r'WhatsApp: \+51 999 888 777',
            f'WhatsApp: {whatsapp}',
            contenido
        )
    
    # Actualizar PayPal
    if paypal_email:
        contenido = re.sub(
            r'consorciodej@gmail\.com',
            paypal_email,
            contenido
        )
    
    if paypal_link:
        contenido = re.sub(
            r'https://paypal\.me/consorciodej',
            paypal_link,
            contenido
        )
    
    # Guardar archivo actualizado
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print("✅ Archivo actualizado exitosamente")

def mostrar_datos_actuales():
    """Mostrar los datos bancarios actuales"""
    
    archivo = "simple_payment_system.py"
    
    if not os.path.exists(archivo):
        print(f"❌ ERROR: No se encontró el archivo {archivo}")
        return
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    print("📋 DATOS BANCARIOS ACTUALES:")
    print("-" * 40)
    
    # Buscar datos bancarios
    banco_match = re.search(r'Banco: (.+)', contenido)
    cuenta_match = re.search(r'Cuenta: (.+)', contenido)
    cci_match = re.search(r'CCI: (.+)', contenido)
    titular_match = re.search(r'Titular: (.+)', contenido)
    
    if banco_match:
        print(f"Banco: {banco_match.group(1)}")
    if cuenta_match:
        print(f"Cuenta: {cuenta_match.group(1)}")
    if cci_match:
        print(f"CCI: {cci_match.group(1)}")
    if titular_match:
        print(f"Titular: {titular_match.group(1)}")
    
    print()
    print("📱 DATOS MÓVILES ACTUALES:")
    print("-" * 40)
    
    # Buscar números móviles
    whatsapp_match = re.search(r'WhatsApp: (.+)', contenido)
    if whatsapp_match:
        print(f"WhatsApp: {whatsapp_match.group(1)}")
    
    # Buscar PayPal
    paypal_match = re.search(r'consorciodej@gmail\.com', contenido)
    if paypal_match:
        print("PayPal: consorciodej@gmail.com")
    else:
        print("PayPal: Configurado personalmente")

if __name__ == "__main__":
    print("🔧 CONFIGURADOR DE DATOS BANCARIOS")
    print("=" * 50)
    print()
    print("1. Configurar datos bancarios")
    print("2. Ver datos actuales")
    print("3. Salir")
    print()
    
    opcion = input("Selecciona una opción (1-3): ").strip()
    
    if opcion == "1":
        configurar_datos_bancarios()
    elif opcion == "2":
        mostrar_datos_actuales()
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
    else:
        print("❌ Opción no válida") 