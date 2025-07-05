#!/usr/bin/env python3
"""
Script de prueba para verificar que la aplicación Streamlit funciona correctamente
"""

import sys
import os

def test_imports():
    """Prueba que todas las importaciones funcionen correctamente"""
    try:
        import streamlit as st
        print("✅ Streamlit importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Streamlit: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando NumPy: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Pandas: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ Matplotlib importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Matplotlib: {e}")
        return False
    
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        print("✅ ReportLab importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando ReportLab: {e}")
        return False
    
    return True

def test_functions():
    """Prueba que las funciones principales funcionen"""
    try:
        # Importar funciones de la aplicación
        sys.path.append(os.path.dirname(__file__))
        from APP import calcular_diseno_fuste, generar_pdf_reportlab, dibujar_muro_streamlit
        
        print("✅ Funciones importadas correctamente")
        
        # Probar cálculo del fuste
        resultados_test = {
            'ka': 0.333,
            'Bz': 2.5,
            'hz': 0.4,
            'b': 0.35,
            'r': 0.7,
            't': 1.45,
            'hm': 1.2
        }
        
        datos_entrada_test = {
            'h1': 2.8,
            'gamma_relleno': 1800,
            'phi_relleno': 30,
            'cohesion': 1.0,
            'Df': 1.2,
            'fc': 210,
            'fy': 4200,
            'qsc': 1000,
            'hm': 1.2
        }
        
        diseno_fuste = calcular_diseno_fuste(resultados_test, datos_entrada_test)
        print("✅ Función calcular_diseno_fuste funciona correctamente")
        
        # Probar generación de PDF
        pdf_buffer = generar_pdf_reportlab(resultados_test, datos_entrada_test, diseno_fuste, "premium")
        print("✅ Función generar_pdf_reportlab funciona correctamente")
        
        # Probar dibujo del muro
        dimensiones_test = {
            'Bz': 2.5,
            'hz': 0.4,
            'b': 0.35,
            'r': 0.7,
            't': 1.45,
            'hm': 1.2
        }
        
        fig = dibujar_muro_streamlit(dimensiones_test, 2.8, 1.2, 1000)
        print("✅ Función dibujar_muro_streamlit funciona correctamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en funciones: {e}")
        return False

def main():
    """Función principal de prueba"""
    print("🧪 INICIANDO PRUEBAS DE LA APLICACIÓN STREAMLIT")
    print("=" * 50)
    
    # Probar importaciones
    print("\n📦 Probando importaciones...")
    if not test_imports():
        print("❌ Fallaron las pruebas de importación")
        return False
    
    # Probar funciones
    print("\n🔧 Probando funciones principales...")
    if not test_functions():
        print("❌ Fallaron las pruebas de funciones")
        return False
    
    print("\n✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    print("🎉 La aplicación está lista para ejecutarse")
    print("\nPara ejecutar la aplicación:")
    print("streamlit run APP.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 