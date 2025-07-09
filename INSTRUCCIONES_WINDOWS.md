# 🏗️ CONSORCIO DEJ - Instalación en Windows

## 🚀 Instalación Rápida en Windows

### Opción 1: Script Automático (Recomendado)

1. **Haz doble clic en el archivo:** `install_dependencies.bat`
2. **Espera a que termine la instalación**
3. **Ejecuta la aplicación:** `streamlit run APP.py`

### Opción 2: Instalación Manual

1. **Abre PowerShell o CMD como administrador**
2. **Navega a la carpeta del proyecto:**
   ```cmd
   cd "C:\Users\selec\Desktop\PROGRAMACION DIGITAL\CONCRETO ARMADO"
   ```

3. **Actualiza pip:**
   ```cmd
   python -m pip install --upgrade pip
   ```

4. **Instala las dependencias:**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Verifica la instalación:**
   ```cmd
   python verify_dependencies.py
   ```

6. **Ejecuta la aplicación:**
   ```cmd
   streamlit run APP.py
   ```

## 🔧 Solución de Problemas en Windows

### Error: "Python no se reconoce como comando"

**Solución:**
1. Descarga Python desde: https://www.python.org/downloads/
2. Durante la instalación, **marca la casilla "Add Python to PATH"**
3. Reinicia PowerShell/CMD
4. Verifica: `python --version`

### Error: "pip no se reconoce como comando"

**Solución:**
```cmd
python -m pip install --upgrade pip
```

### Error: "reportlab no está instalado"

**Solución:**
```cmd
pip install reportlab>=4.0.0
```

### Error: "matplotlib no está instalado"

**Solución:**
```cmd
pip install matplotlib>=3.7.0
```

### Error: "plotly no está instalado"

**Solución:**
```cmd
pip install plotly>=5.15.0
```

### Error: "streamlit no está instalado"

**Solución:**
```cmd
pip install streamlit>=1.28.0
```

## 📋 Verificación Completa

Para verificar que todo esté funcionando:

```cmd
python verify_dependencies.py
```

Deberías ver algo como:
```
🔍 CONSORCIO DEJ - Verificador de Dependencias
==================================================
📦 Verificando dependencias...

✅ Streamlit - INSTALADO
✅ Pandas - INSTALADO
✅ NumPy - INSTALADO
✅ Matplotlib - INSTALADO
✅ Plotly - INSTALADO
✅ ReportLab - INSTALADO
...

📊 Resumen: 13/13 dependencias instaladas
🎉 ¡Todas las dependencias están instaladas correctamente!
```

## 🚀 Ejecutar la Aplicación

Una vez instaladas todas las dependencias:

```cmd
streamlit run APP.py
```

La aplicación se abrirá automáticamente en tu navegador en:
- **URL:** http://localhost:8501

## 🔐 Credenciales de Acceso

### Usuario Administrador (Acceso Completo)
- **Usuario:** admin
- **Contraseña:** admin123

### Usuario Demo (Acceso Básico)
- **Usuario:** demo
- **Contraseña:** demo

## 📱 Características Disponibles

### Plan Gratuito
- ✅ Cálculos básicos de análisis estructural
- ✅ Resultados simples con gráficos básicos
- ✅ Reporte básico descargable
- ✅ Análisis de propiedades de materiales

### Plan Premium (con credenciales admin)
- ⭐ Análisis completo con ACI 318-2025
- ⭐ Cálculos de predimensionamiento automáticos
- ⭐ Reportes técnicos en PDF
- ⭐ Gráficos interactivos avanzados
- ⭐ Verificaciones de estabilidad completas
- ⭐ Fórmulas de diseño estructural detalladas

## 🆘 Soporte Técnico

Si encuentras problemas:

1. **Ejecuta el verificador:**
   ```cmd
   python verify_dependencies.py
   ```

2. **Reinstala las dependencias:**
   ```cmd
   pip install --force-reinstall -r requirements.txt
   ```

3. **Contacta soporte:**
   - Email: contacto@consorciodej.com
   - WhatsApp: +51 999 888 777

## 📄 Archivos Importantes

- `APP.py` - Aplicación principal
- `requirements.txt` - Lista de dependencias
- `install_dependencies.bat` - Instalador automático
- `verify_dependencies.py` - Verificador de instalación
- `README_INSTALACION.md` - Instrucciones completas

---

**🏗️ CONSORCIO DEJ - Ingeniería y Construcción Especializada** 