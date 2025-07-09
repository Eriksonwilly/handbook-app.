# 🏗️ CONSORCIO DEJ - Instrucciones de Instalación

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet para descargar dependencias

## 🚀 Instalación Rápida

### Opción 1: Script Automático (Recomendado)

```bash
# Ejecutar el script de instalación automática
python install_dependencies.py
```

### Opción 2: Instalación Manual

```bash
# Instalar todas las dependencias desde requirements.txt
pip install -r requirements.txt
```

### Opción 3: Instalación Individual

```bash
# Dependencias principales
pip install streamlit>=1.28.0
pip install pandas>=2.0.0
pip install numpy>=1.24.0
pip install matplotlib>=3.7.0
pip install plotly>=5.15.0
pip install reportlab>=4.0.0

# Dependencias adicionales
pip install openpyxl>=3.1.0
pip install stripe>=7.0.0
pip install streamlit-authenticator>=0.2.0
pip install streamlit-option-menu>=0.3.0
pip install Pillow>=10.0.0
pip install scipy>=1.10.0
pip install seaborn>=0.12.0
```

## 🔍 Verificación de Instalación

Para verificar que todas las dependencias están instaladas correctamente:

```bash
python -c "import streamlit, pandas, numpy, matplotlib, plotly, reportlab; print('✅ Todas las dependencias están disponibles')"
```

## 🚀 Ejecutar la Aplicación

```bash
# Ejecutar la aplicación principal
streamlit run APP.py
```

## 🌐 Acceso Web

Una vez ejecutada la aplicación, se abrirá automáticamente en tu navegador en:
- **URL Local:** http://localhost:8501
- **URL de Red:** http://[tu-ip]:8501

## 🔧 Solución de Problemas

### Error: "reportlab no está instalado"

```bash
# Solución 1: Instalar reportlab específicamente
pip install reportlab>=4.0.0

# Solución 2: Actualizar pip primero
python -m pip install --upgrade pip
pip install reportlab>=4.0.0
```

### Error: "matplotlib no está instalado"

```bash
# Instalar matplotlib
pip install matplotlib>=3.7.0

# En sistemas Linux, también instalar dependencias del sistema
sudo apt-get install python3-tk  # Ubuntu/Debian
```

### Error: "plotly no está instalado"

```bash
# Instalar plotly
pip install plotly>=5.15.0
```

### Error: "streamlit no está instalado"

```bash
# Instalar streamlit
pip install streamlit>=1.28.0
```

## 📦 Dependencias Principales

| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| streamlit | >=1.28.0 | Framework web para la aplicación |
| pandas | >=2.0.0 | Manipulación de datos |
| numpy | >=1.24.0 | Cálculos numéricos |
| matplotlib | >=3.7.0 | Gráficos estáticos |
| plotly | >=5.15.0 | Gráficos interactivos |
| reportlab | >=4.0.0 | Generación de PDFs |
| openpyxl | >=3.1.0 | Manejo de archivos Excel |
| Pillow | >=10.0.0 | Procesamiento de imágenes |
| scipy | >=1.10.0 | Funciones científicas |
| seaborn | >=0.12.0 | Gráficos estadísticos |

## 🔐 Credenciales de Acceso

### Usuario Administrador (Acceso Completo)
- **Usuario:** admin
- **Contraseña:** admin123

### Usuario Demo (Acceso Básico)
- **Usuario:** demo
- **Contraseña:** demo

## 📱 Características por Plan

### Plan Gratuito
- ✅ Cálculos básicos de análisis estructural
- ✅ Resultados simples con gráficos básicos
- ✅ Reporte básico descargable
- ✅ Análisis de propiedades de materiales

### Plan Premium
- ⭐ Análisis completo con ACI 318-2025
- ⭐ Cálculos de predimensionamiento automáticos
- ⭐ Reportes técnicos en PDF
- ⭐ Gráficos interactivos avanzados
- ⭐ Verificaciones de estabilidad completas
- ⭐ Fórmulas de diseño estructural detalladas

## 🆘 Soporte

Si encuentras problemas durante la instalación:

1. **Verifica la versión de Python:**
   ```bash
   python --version
   ```

2. **Actualiza pip:**
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Instala en un entorno virtual (recomendado):**
   ```bash
   python -m venv consorcio_dej_env
   source consorcio_dej_env/bin/activate  # Linux/Mac
   consorcio_dej_env\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

4. **Contacta soporte técnico:**
   - Email: contacto@consorciodej.com
   - WhatsApp: +51 999 888 777

## 📄 Licencia

Este software es propiedad de CONSORCIO DEJ. Todos los derechos reservados.

---

**🏗️ CONSORCIO DEJ - Ingeniería y Construcción Especializada** 