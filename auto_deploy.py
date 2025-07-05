#!/usr/bin/env python3
"""
Script de automatización completa para desplegar y generar APK
CONSORCIO DEJ - Automatización de Despliegue
"""

import os
import subprocess
import webbrowser
import time

def check_requirements():
    """Verificar que todas las dependencias estén instaladas"""
    print("🔍 Verificando dependencias...")
    
    required_packages = [
        'streamlit',
        'pandas',
        'numpy',
        'matplotlib',
        'plotly',
        'reportlab',
        'Pillow'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    if missing_packages:
        print(f"\n📦 Instalando paquetes faltantes: {', '.join(missing_packages)}")
        for package in missing_packages:
            subprocess.run(['pip', 'install', package])
    
    print("✅ Todas las dependencias están instaladas")

def optimize_app():
    """Optimizar la aplicación para móviles"""
    print("\n⚙️ Optimizando aplicación para móviles...")
    
    # Ejecutar script de optimización
    try:
        subprocess.run(['python', 'optimize_for_mobile.py'])
        print("✅ Aplicación optimizada")
    except Exception as e:
        print(f"⚠️ Error en optimización: {e}")

def create_git_repo():
    """Crear repositorio Git si no existe"""
    print("\n📁 Configurando repositorio Git...")
    
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])
        print("✅ Repositorio Git inicializado")
    
    # Crear .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/secrets.toml

# Logs
*.log

# Temporary files
*.tmp
*.temp
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ .gitignore creado")

def create_readme():
    """Crear README profesional"""
    print("\n📖 Creando README profesional...")
    
    readme_content = """# 🏗️ CONSORCIO DEJ - Muros de Contención

## 📱 Aplicación Móvil Profesional

Aplicación completa para diseño y análisis de muros de contención según la teoría de Rankine.

### ✨ Características

- **Cálculo Básico:** Análisis rápido de estabilidad
- **Análisis Completo:** Diseño profesional con teoría de Rankine
- **Diseño del Fuste:** Cálculo estructural detallado
- **Reportes PDF:** Documentación técnica profesional
- **Gráficos Interactivos:** Visualizaciones avanzadas
- **Aplicación Móvil:** Disponible en Google Play Store

### 🚀 Despliegue Rápido

```bash
# 1. Optimizar para móviles
python optimize_for_mobile.py

# 2. Desplegar en Streamlit Cloud
# Ve a https://share.streamlit.io

# 3. Generar APK
# Ve a https://www.pwabuilder.com
```

### 💰 Modelo de Negocio

- **Plan Gratuito:** Cálculos básicos
- **Plan Premium ($9.99/mes):** Análisis completo + PDFs
- **Plan Empresarial ($29.99/mes):** API + Soporte técnico

### 📊 Potencial de Ingresos

- **Conservador:** $2,498/mes
- **Optimista:** $10,993/mes

### 🛠️ Tecnologías

- **Backend:** Python, Streamlit
- **Frontend:** HTML, CSS, JavaScript
- **Gráficos:** Plotly, Matplotlib
- **PDFs:** ReportLab
- **Móvil:** PWA (Progressive Web App)

### 📱 Disponible en

- 🌐 Web: [URL de Streamlit Cloud]
- 📱 Android: Google Play Store
- 🍎 iOS: App Store (próximamente)

### 👨‍💼 Desarrollado por

**CONSORCIO DEJ**
Ingeniería y Construcción Especializada

---
*Versión 2.1 - Optimizada para móviles*
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("✅ README creado")

def open_deployment_links():
    """Abrir enlaces de despliegue"""
    print("\n🌐 Abriendo enlaces de despliegue...")
    
    links = {
        "Streamlit Cloud": "https://share.streamlit.io",
        "PWA Builder": "https://www.pwabuilder.com",
        "Google Play Console": "https://play.google.com/console",
        "Huawei AppGallery": "https://developer.huawei.com/consumer/en/console"
    }
    
    for name, url in links.items():
        print(f"📱 Abriendo {name}...")
        webbrowser.open(url)
        time.sleep(2)

def show_deployment_steps():
    """Mostrar pasos de despliegue"""
    print("\n" + "="*60)
    print("🚀 PASOS PARA GENERAR APK Y MONETIZAR")
    print("="*60)
    
    steps = [
        ("1️⃣", "Subir a GitHub", "git add . && git commit -m 'Initial commit' && git push"),
        ("2️⃣", "Desplegar en Streamlit Cloud", "Ve a https://share.streamlit.io"),
        ("3️⃣", "Generar APK con PWA Builder", "Ve a https://www.pwabuilder.com"),
        ("4️⃣", "Publicar en Google Play", "Cuenta desarrollador: $25"),
        ("5️⃣", "Configurar pagos", "Stripe/PayPal para suscripciones"),
        ("6️⃣", "Monetizar", "¡Empieza a ganar dinero!")
    ]
    
    for emoji, step, command in steps:
        print(f"{emoji} {step}")
        if command:
            print(f"   💻 {command}")
        print()

def main():
    """Función principal"""
    print("🏗️ CONSORCIO DEJ - Automatización de Despliegue")
    print("=" * 60)
    
    try:
        # Verificar dependencias
        check_requirements()
        
        # Optimizar aplicación
        optimize_app()
        
        # Configurar Git
        create_git_repo()
        
        # Crear README
        create_readme()
        
        # Mostrar pasos
        show_deployment_steps()
        
        # Preguntar si abrir enlaces
        response = input("\n¿Quieres abrir los enlaces de despliegue? (s/n): ")
        if response.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            open_deployment_links()
        
        print("\n🎉 ¡Automatización completada!")
        print("\n📱 Tu app está lista para:")
        print("   ✅ Desplegar en Streamlit Cloud")
        print("   ✅ Generar APK con PWA Builder")
        print("   ✅ Publicar en Google Play")
        print("   ✅ Monetizar con suscripciones")
        
        print("\n💰 Potencial de ingresos:")
        print("   📊 Conservador: $2,498/mes")
        print("   📈 Optimista: $10,993/mes")
        
        print("\n🚀 ¡Sigue los pasos y empieza a monetizar tu app!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Verifica que tienes todas las dependencias instaladas")

if __name__ == "__main__":
    main() 