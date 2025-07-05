# 🔧 SOLUCIÓN ERROR STREAMLIT - LÍNEAS 14-17

## 🚨 **PROBLEMA IDENTIFICADO**
```
streamlit run APP.py
~~~~~~~~~
CategoryInfo: ObjectNotFound: (streamlit:String) [], CommandNotFoundException
```

**CAUSA:** Streamlit no está instalado o no está en el PATH del sistema.

---

## ✅ **SOLUCIONES (en orden de preferencia)**

### **OPCIÓN 1: Script automático (MÁS FÁCIL)**
1. **Doble clic en:** `EJECUTAR_APP.bat`
2. **O ejecuta:** `INSTALAR_TODO.bat` primero

### **OPCIÓN 2: Instalación manual**
```bash
# Abrir terminal en la carpeta HANDBOOK
cd HANDBOOK

# Instalar streamlit
pip install streamlit

# Verificar instalación
pip list | findstr streamlit
```

### **OPCIÓN 3: Si la opción 2 no funciona**
```bash
python -m pip install streamlit
```

### **OPCIÓN 4: Si estás en entorno virtual**
```bash
# Activar entorno virtual
venv\Scripts\activate

# Instalar streamlit
pip install streamlit
```

---

## 🚀 **EJECUTAR LA APLICACIÓN**

### **Método 1: Script automático**
```bash
# Doble clic en EJECUTAR_APP.bat
```

### **Método 2: Comando directo**
```bash
cd HANDBOOK
streamlit run APP.py
```

### **Método 3: Si el método 2 no funciona**
```bash
cd HANDBOOK
python -m streamlit run APP.py
```

### **Método 4: Con puerto específico**
```bash
cd HANDBOOK
python -m streamlit run APP.py --server.port 8501
```

---

## 🔍 **VERIFICACIÓN**

### **Verificar que Python esté instalado:**
```bash
python --version
```

### **Verificar que pip esté instalado:**
```bash
pip --version
```

### **Verificar que streamlit esté instalado:**
```bash
pip list | findstr streamlit
```

---

## 🎯 **PASOS COMPLETOS**

### **1. Abrir terminal en la carpeta HANDBOOK**
```bash
cd HANDBOOK
```

### **2. Instalar streamlit**
```bash
pip install streamlit
```

### **3. Ejecutar aplicación**
```bash
python -m streamlit run APP.py
```

### **4. Abrir navegador**
```
http://localhost:8501
```

### **5. Iniciar sesión**
```
Usuario: admin
Contraseña: admin123
```

---

## 🚨 **SI NADA FUNCIONA**

### **Verificar que estés en la carpeta correcta:**
```bash
dir
# Debe mostrar: APP.py, simple_payment_system.py, etc.
```

### **Verificar que Python esté en el PATH:**
```bash
where python
```

### **Reinstalar Python:**
1. Descargar Python desde: https://python.org
2. Instalar con "Add to PATH" marcado
3. Reiniciar terminal
4. Ejecutar: `pip install streamlit`

---

## 📱 **CONTACTO PARA SOPORTE**

- **WhatsApp:** +51 999 888 777
- **Email:** consorciodej@gmail.com

**¡Solución garantizada!** 🎉 