#!/usr/bin/env python3
"""
Script para instalar todas las dependencias necesarias para CONSORCIO DEJ
Análisis Estructural
"""

import subprocess
import sys
import os

def install_package(package):
    """Instala un paquete usando pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} instalado correctamente")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error instalando {package}")
        return False

def main():
    print("🏗️ CONSORCIO DEJ - Instalador de Dependencias")
    print("=" * 50)
    
    # Lista de dependencias principales
    dependencies = [
        "streamlit>=1.28.0",
        "pandas>=2.0.0", 
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "plotly>=5.15.0",
        "reportlab>=4.0.0",
        "openpyxl>=3.1.0",
        "stripe>=7.0.0",
        "streamlit-authenticator>=0.2.0",
        "streamlit-option-menu>=0.3.0",
        "Pillow>=10.0.0",
        "scipy>=1.10.0",
        "seaborn>=0.12.0"
    ]
    
    print("📦 Instalando dependencias...")
    print()
    
    success_count = 0
    total_count = len(dependencies)
    
    for dep in dependencies:
        print(f"Instalando {dep}...")
        if install_package(dep):
            success_count += 1
        print()
    
    print("=" * 50)
    print(f"📊 Resumen: {success_count}/{total_count} dependencias instaladas")
    
    if success_count == total_count:
        print("🎉 ¡Todas las dependencias se instalaron correctamente!")
        print("🚀 Puedes ejecutar la aplicación con: streamlit run APP.py")
    else:
        print("⚠️ Algunas dependencias no se pudieron instalar.")
        print("💡 Intenta ejecutar manualmente: pip install -r requirements.txt")
    
    print()
    print("📋 Para verificar la instalación, ejecuta:")
    print("python -c \"import streamlit, pandas, numpy, matplotlib, plotly, reportlab; print('✅ Todas las dependencias están disponibles')\"")

if __name__ == "__main__":
    main() 