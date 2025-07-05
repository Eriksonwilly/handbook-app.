#!/usr/bin/env python3
"""
Script para activar acceso completo del administrador
CONSORCIO DEJ - Muros de Contención
"""

import streamlit as st
import os
import json

def activar_admin_completo():
    """Activar acceso completo para el administrador"""
    
    st.title("🔧 ACTIVACIÓN DE ADMINISTRADOR COMPLETO")
    st.subheader("CONSORCIO DEJ - Muros de Contención")
    
    st.info("Este script activa el acceso completo para el administrador")
    
    # Verificar si existe el archivo de configuración
    config_file = "admin_config.json"
    
    if st.button("🚀 ACTIVAR ACCESO COMPLETO", type="primary"):
        
        # Crear configuración de administrador
        admin_config = {
            "admin_user": "admin",
            "admin_password": "admin123",
            "admin_plan": "empresarial",
            "admin_access": "completo",
            "bypass_payment": True,
            "direct_access": True
        }
        
        # Guardar configuración
        try:
            with open(config_file, 'w') as f:
                json.dump(admin_config, f, indent=2)
            
            st.success("✅ Configuración de administrador guardada")
            
            # Mostrar instrucciones
            st.markdown("""
            ### 📋 INSTRUCCIONES PARA ACCESO COMPLETO:
            
            1. **Cierra la aplicación actual** (si está corriendo)
            2. **Ejecuta la aplicación principal:**
               ```bash
               streamlit run APP.py
               ```
            3. **Inicia sesión como administrador:**
               - Usuario: `admin`
               - Contraseña: `admin123`
            
            4. **Acceso directo desde el sidebar:**
               - Verás un panel especial de administrador
               - Botones para activar cualquier plan directamente
               - No necesitas pasar por el sistema de pagos
            
            5. **Funciones disponibles:**
               - ✅ Análisis completo
               - ✅ Diseño del fuste
               - ✅ Reportes PDF
               - ✅ Gráficos avanzados
               - ✅ Todas las funciones premium y empresarial
            
            ### 🔑 CREDENCIALES DE ADMINISTRADOR:
            - **Usuario:** admin
            - **Contraseña:** admin123
            - **Plan:** Empresarial (acceso completo)
            """)
            
        except Exception as e:
            st.error(f"❌ Error guardando configuración: {str(e)}")
    
    # Mostrar estado actual
    if os.path.exists(config_file):
        st.success("✅ Configuración de administrador ya existe")
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            st.json(config)
            
        except Exception as e:
            st.error(f"❌ Error leyendo configuración: {str(e)}")
    else:
        st.warning("⚠️ No hay configuración de administrador")
    
    # Botón para limpiar configuración
    if st.button("🗑️ Limpiar Configuración"):
        if os.path.exists(config_file):
            os.remove(config_file)
            st.success("✅ Configuración eliminada")
            st.rerun()
        else:
            st.info("No hay configuración para eliminar")

if __name__ == "__main__":
    activar_admin_completo() 