#!/usr/bin/env python3
"""
Script de instalación automática de dependencias para CONSORCIO DEJ
"""

import subprocess
import sys
import importlib

def check_package(package_name):
    """Verifica si un paquete está instalado"""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def install_package(package_name):
    """Instala un paquete usando pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🔧 CONSORCIO DEJ - Instalador de Dependencias")
    print("=" * 50)
    
    # Lista de paquetes requeridos
    required_packages = [
        "streamlit",
        "numpy", 
        "pandas",
        "matplotlib",
        "plotly",
        "reportlab"
    ]
    
    missing_packages = []
    
    # Verificar paquetes instalados
    print("📋 Verificando paquetes instalados...")
    for package in required_packages:
        if check_package(package):
            print(f"✅ {package} - Instalado")
        else:
            print(f"❌ {package} - Faltante")
            missing_packages.append(package)
    
    if not missing_packages:
        print("\n🎉 ¡Todas las dependencias están instaladas!")
        print("Puedes ejecutar la aplicación con: streamlit run APP.py")
        return
    
    # Instalar paquetes faltantes
    print(f"\n📦 Instalando {len(missing_packages)} paquetes faltantes...")
    
    for package in missing_packages:
        print(f"\n🔧 Instalando {package}...")
        if install_package(package):
            print(f"✅ {package} instalado correctamente")
        else:
            print(f"❌ Error al instalar {package}")
            print("Intenta instalarlo manualmente:")
            print(f"pip install {package}")
    
    print("\n🎯 Instalación completada!")
    print("Ejecuta la aplicación con: streamlit run APP.py")

if __name__ == "__main__":
    main() 