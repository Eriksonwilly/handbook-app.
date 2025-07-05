# 💰 CONFIGURACIÓN DE PAGOS - CONSORCIO DEJ

## 🏦 **CONFIGURAR TUS DATOS BANCARIOS REALES**

### **PASO 1: Editar datos bancarios**

Abre el archivo `simple_payment_system.py` y busca la línea donde dice:

```python
elif method == "transferencia":
    return f"""
🏦 TRANSFERENCIA BANCÁRIA (PERÚ)
💰 Monto: S/{(amount * 3.7):.2f} PEN

📋 DATOS BANCARIOS REALES - TU CUENTA BCP:
Banco: BCP
Cuenta: 193-12345678-0-12          # ← CAMBIAR POR TU CUENTA
CCI: 002-193-001234567890-12       # ← CAMBIAR POR TU CCI
Titular: CONSORCIO DEJ SAC         # ← CAMBIAR POR TU NOMBRE
```

### **PASO 2: Reemplazar con tus datos reales**

```python
# EJEMPLO CON TUS DATOS REALES:
Banco: BCP
Cuenta: 193-87654321-0-12          # Tu número de cuenta
CCI: 002-193-008765432109-12       # Tu CCI
Titular: TU NOMBRE COMPLETO         # Tu nombre real
```

### **PASO 3: Configurar Yape y PLIN**

Busca las líneas:
```python
elif method == "yape":
    # Cambiar: +51 999 888 777 por tu número real
    # Ejemplo: +51 987 654 321

elif method == "plin":
    # Cambiar: +51 999 888 777 por tu número real
    # Ejemplo: +51 987 654 321
```

### **PASO 4: Configurar PayPal**

Busca la línea:
```python
elif method == "paypal":
    # Cambiar: consorciodej@gmail.com por tu email real
    # Ejemplo: tuemail@gmail.com
```

---

## 📱 **CONFIGURAR WHATSAPP**

### **Cambiar número de WhatsApp:**

Busca todas las líneas que digan:
```python
WhatsApp: +51 999 888 777
```

Y reemplázalas por tu número real:
```python
WhatsApp: +51 987 654 321
```

---

## 🎯 **DATOS A CONFIGURAR**

### **1. Datos Bancarios BCP:**
- ✅ Número de cuenta
- ✅ CCI (Código de Cuenta Interbancario)
- ✅ Nombre del titular

### **2. Datos de Pago Móvil:**
- ✅ Número de Yape
- ✅ Número de PLIN
- ✅ Número de WhatsApp

### **3. Datos de PayPal:**
- ✅ Email de PayPal
- ✅ Link de PayPal.me

---

## 🔧 **ARCHIVO DE CONFIGURACIÓN RÁPIDA**

Crea un archivo `config_pagos.py`:

```python
# CONFIGURACIÓN DE PAGOS - CONSORCIO DEJ
# Reemplaza estos datos con los tuyos reales

BANK_DATA = {
    "banco": "BCP",
    "cuenta": "193-87654321-0-12",  # Tu cuenta real
    "cci": "002-193-008765432109-12",  # Tu CCI real
    "titular": "TU NOMBRE COMPLETO"  # Tu nombre real
}

MOBILE_DATA = {
    "yape": "+51 987 654 321",  # Tu número Yape
    "plin": "+51 987 654 321",  # Tu número PLIN
    "whatsapp": "+51 987 654 321"  # Tu WhatsApp
}

PAYPAL_DATA = {
    "email": "tuemail@gmail.com",  # Tu email PayPal
    "link": "https://paypal.me/tuusuario"  # Tu link PayPal.me
}
```

---

## ✅ **VERIFICACIÓN**

### **Después de configurar:**

1. **Ejecuta la aplicación:**
   ```bash
   python -m streamlit run APP.py
   ```

2. **Ve a "Cambiar Plan" → "Empresarial"**

3. **Selecciona "Transferencia Bancaria"**

4. **Verifica que aparezcan tus datos reales**

---

## 🚨 **IMPORTANTE**

- ✅ **Nunca compartas** tus datos bancarios en código público
- ✅ **Usa variables de entorno** para datos sensibles
- ✅ **Verifica** que los datos sean correctos antes de publicar
- ✅ **Prueba** el proceso de pago con un monto pequeño

---

## 📞 **SOPORTE**

Si necesitas ayuda para configurar:
- **WhatsApp:** +51 987 654 321
- **Email:** tuemail@gmail.com

**¡Configuración garantizada!** 🎉 