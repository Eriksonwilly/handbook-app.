#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias estén instaladas correctamente
"""

import importlib
import sys

def check_dependency(module_name, package_name=None):
    """Verifica si una dependencia está instalada"""
    if package_name is None:
        package_name = module_name
    
    try:
        importlib.import_module(module_name)
        print(f"✅ {package_name} - INSTALADO")
        return True
    except ImportError:
        print(f"❌ {package_name} - NO INSTALADO")
        return False

def main():
    print("🔍 CONSORCIO DEJ - Verificador de Dependencias")
    print("=" * 50)
    
    # Lista de dependencias a verificar
    dependencies = [
        ("streamlit", "Streamlit"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("plotly", "Plotly"),
        ("reportlab", "ReportLab"),
        ("openpyxl", "OpenPyXL"),
        ("stripe", "Stripe"),
        ("streamlit_authenticator", "Streamlit-Authenticator"),
        ("streamlit_option_menu", "Streamlit-Option-Menu"),
        ("PIL", "Pillow"),
        ("scipy", "SciPy"),
        ("seaborn", "Seaborn")
    ]
    
    print("📦 Verificando dependencias...")
    print()
    
    installed_count = 0
    total_count = len(dependencies)
    
    for module, package in dependencies:
        if check_dependency(module, package):
            installed_count += 1
    
    print()
    print("=" * 50)
    print(f"📊 Resumen: {installed_count}/{total_count} dependencias instaladas")
    
    if installed_count == total_count:
        print("🎉 ¡Todas las dependencias están instaladas correctamente!")
        print("🚀 La aplicación debería funcionar sin problemas.")
    else:
        print("⚠️ Faltan algunas dependencias.")
        print("💡 Ejecuta: python install_dependencies.py")
        print("💡 O instala manualmente: pip install -r requirements.txt")
    
    print()
    
    # Verificaciones adicionales
    print("🔧 Verificaciones adicionales:")
    
    # Verificar versión de Python
    python_version = sys.version_info
    print(f"🐍 Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version >= (3, 8):
        print("✅ Versión de Python compatible")
    else:
        print("❌ Se requiere Python 3.8 o superior")
    
    # Verificar si matplotlib puede generar gráficos
    try:
        import matplotlib
        matplotlib.use('Agg')  # Backend no interactivo
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        plt.close(fig)
        print("✅ Matplotlib configurado correctamente")
    except Exception as e:
        print(f"❌ Error con Matplotlib: {e}")
    
    # Verificar si reportlab puede generar PDFs
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate
        print("✅ ReportLab configurado correctamente")
    except Exception as e:
        print(f"❌ Error con ReportLab: {e}")
    
    print()
    print("📋 Para instalar dependencias faltantes:")
    print("python install_dependencies.py")
    print()
    print("📋 Para ejecutar la aplicación:")
    print("streamlit run APP.py")

if __name__ == "__main__":
    main() 