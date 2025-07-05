#!/usr/bin/env python3
"""
Script para instalar dependencias y ejecutar la aplicación
CONSORCIO DEJ - Muros de Contención
"""

import subprocess
import sys
import os

def ejecutar_comando(comando, descripcion):
    """Ejecutar un comando y mostrar el resultado"""
    print(f"[INFO] {descripcion}...")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {descripcion} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {descripcion}: {e}")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("=" * 50)
    print("   CONSORCIO DEJ - INSTALACION COMPLETA")
    print("=" * 50)
    print()
    
    # Verificar Python
    print(f"[INFO] Versión de Python: {sys.version}")
    
    # Crear entorno virtual si no existe
    if not os.path.exists("venv"):
        print("[1/5] Creando entorno virtual...")
        if not ejecutar_comando("python -m venv venv", "Crear entorno virtual"):
            return False
    else:
        print("[1/5] Entorno virtual ya existe...")
    
    # Activar entorno virtual e instalar dependencias
    print("[2/5] Activando entorno virtual...")
    
    # Determinar el comando de activación según el sistema operativo
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Linux/Mac
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Instalar dependencias
    print("[3/5] Instalando dependencias...")
    
    dependencias = [
        "streamlit>=1.28.0",
        "pandas>=2.0.0", 
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "plotly>=5.15.0",
        "reportlab>=4.0.0",
        "openpyxl>=3.1.0"
    ]
    
    for dep in dependencias:
        if not ejecutar_comando(f"{pip_cmd} install {dep}", f"Instalar {dep}"):
            print(f"⚠️ Continuando sin {dep}")
    
    print("[4/5] Verificando instalación...")
    if not ejecutar_comando(f"{pip_cmd} list", "Listar paquetes instalados"):
        print("⚠️ No se pudo verificar la instalación")
    
    print("[5/5] Iniciando aplicación...")
    print()
    print("=" * 50)
    print("   CREDENCIALES DE ADMINISTRADOR")
    print("=" * 50)
    print()
    print("Usuario: admin")
    print("Contraseña: admin123")
    print("Plan: Empresarial (acceso completo)")
    print()
    print("=" * 50)
    print("   FUNCIONES DISPONIBLES")
    print("=" * 50)
    print()
    print("✅ Análisis completo")
    print("✅ Diseño del fuste")
    print("✅ Reportes PDF")
    print("✅ Gráficos avanzados")
    print("✅ Todas las funciones premium")
    print()
    print("La aplicación se abrirá en tu navegador...")
    print()
    
    input("Presiona Enter para continuar...")
    
    # Ejecutar la aplicación
    print("🚀 Ejecutando aplicación...")
    if os.name == 'nt':  # Windows
        streamlit_cmd = "venv\\Scripts\\streamlit"
    else:  # Linux/Mac
        streamlit_cmd = "venv/bin/streamlit"
    
    try:
        subprocess.run(f"{streamlit_cmd} run APP.py", shell=True)
    except KeyboardInterrupt:
        print("\n👋 Aplicación cerrada por el usuario")
    except Exception as e:
        print(f"❌ Error ejecutando la aplicación: {e}")

if __name__ == "__main__":
    main() 