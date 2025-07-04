import streamlit as st
import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="CONSORCIO DEJ - Muros de Contención",
    page_icon="🏗️",
    layout="wide"
)

# Header con fondo amarillo
st.markdown("""
<div style="text-align: center; padding: 20px; background-color: #FFD700; color: #2F2F2F; border-radius: 10px; margin-bottom: 20px; border: 2px solid #FFA500;">
    <h1>🏗️ CONSORCIO DEJ</h1>
    <p style="font-size: 18px; font-weight: bold;">Ingeniería y Construcción</p>
    <p style="font-size: 14px;">Diseño y Análisis de Muros de Contención</p>
</div>
""", unsafe_allow_html=True)

# Autenticación simple
def login():
    st.title("Iniciar Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if username == "demo" and password == "demo":
            st.session_state['logged_in'] = True
            st.session_state['user'] = username
            st.session_state['plan'] = "gratuito"
        elif username == "premium" and password == "premium":
            st.session_state['logged_in'] = True
            st.session_state['user'] = username
            st.session_state['plan'] = "premium"
        else:
            st.error("Usuario o contraseña incorrectos")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    st.success(f"Bienvenido, {st.session_state['user']}!")
    
    # Botón para cerrar sesión
    if st.sidebar.button("🚪 Cerrar Sesión"):
        st.session_state['logged_in'] = False
        st.session_state['user'] = None
        st.session_state['plan'] = None
        st.rerun()
    
    # Sidebar para navegación
    st.sidebar.title("📋 Menú Principal")
    
    # Mostrar plan actual
    if st.session_state['plan'] == "gratuito":
        st.sidebar.info("🆓 Plan Gratuito")
    else:
        st.sidebar.success("⭐ Plan Premium")
    
    opcion = st.sidebar.selectbox("Selecciona una opción", 
                                 ["🏗️ Cálculo Básico", "📊 Análisis Completo", "📄 Generar Reporte", "📈 Gráficos", "ℹ️ Acerca de", "✉️ Contacto"])

    if opcion == "🏗️ Cálculo Básico":
        st.title("Cálculo Básico de Muro de Contención")
        st.info("Plan gratuito: Cálculos básicos de estabilidad")
        
        # Pestañas para diferentes tipos de cálculos
        tab1, tab2, tab3 = st.tabs(["📏 Dimensiones", "🏗️ Materiales", "⚖️ Cargas"])
        
        with tab1:
            st.subheader("Dimensiones del Muro")
            col1, col2 = st.columns(2)
            with col1:
                altura = st.number_input("Altura del muro (m)", min_value=1.0, max_value=15.0, value=3.0, step=0.1)
                base = st.number_input("Base del muro (m)", min_value=0.5, max_value=8.0, value=1.0, step=0.1)
            with col2:
                espesor = st.number_input("Espesor del muro (m)", min_value=0.2, max_value=2.0, value=0.3, step=0.05)
                longitud = st.number_input("Longitud del muro (m)", min_value=1.0, max_value=100.0, value=10.0, step=0.5)
        
        with tab2:
            st.subheader("Propiedades de los Materiales")
            col1, col2 = st.columns(2)
            with col1:
                peso_especifico = st.number_input("Peso específico del hormigón (kN/m³)", min_value=20.0, max_value=30.0, value=24.0, step=0.5)
                resistencia_concreto = st.number_input("Resistencia del hormigón (MPa)", min_value=15.0, max_value=50.0, value=25.0, step=1.0)
            with col2:
                peso_suelo = st.number_input("Peso específico del suelo (kN/m³)", min_value=15.0, max_value=22.0, value=18.0, step=0.5)
                angulo_friccion = st.number_input("Ángulo de fricción del suelo (°)", min_value=20.0, max_value=45.0, value=30.0, step=1.0)
        
        with tab3:
            st.subheader("Cargas y Factores de Seguridad")
            col1, col2 = st.columns(2)
            with col1:
                sobrecarga = st.number_input("Sobrecarga (kN/m²)", min_value=0.0, max_value=50.0, value=10.0, step=1.0)
                factor_seguridad = st.number_input("Factor de seguridad", min_value=1.2, max_value=3.0, value=1.5, step=0.1)
            with col2:
                sismo = st.checkbox("Considerar sismo")
                viento = st.checkbox("Considerar viento")
        
        # Botón para calcular
        if st.button("🚀 Calcular Muro de Contención", type="primary"):
            # Cálculos básicos
            volumen = altura * base * espesor * longitud
            peso_muro = volumen * peso_especifico
            
            # Cálculo del empuje del suelo
            angulo_rad = math.radians(angulo_friccion)
            ka = math.tan(math.radians(45 - angulo_friccion/2))**2  # Coeficiente de empuje activo
            empuje_suelo = 0.5 * peso_suelo * altura**2 * ka * longitud
            
            # Cálculo del momento volcador
            momento_volcador = empuje_suelo * altura / 3
            
            # Cálculo del momento estabilizador
            momento_estabilizador = peso_muro * base / 2
            
            # Factor de seguridad al volcamiento
            fs_volcamiento = momento_estabilizador / momento_volcador
            
            # Guardar resultados en session state
            st.session_state['resultados_basicos'] = {
                'altura': altura,
                'base': base,
                'espesor': espesor,
                'longitud': longitud,
                'peso_muro': peso_muro,
                'empuje_suelo': empuje_suelo,
                'fs_volcamiento': fs_volcamiento,
                'volumen': volumen,
                'ka': ka,
                'momento_volcador': momento_volcador,
                'momento_estabilizador': momento_estabilizador
            }
            
            st.success("¡Cálculos básicos completados exitosamente!")
            st.balloons()
            
            # MOSTRAR RESULTADOS INMEDIATAMENTE DESPUÉS DEL CÁLCULO
            st.subheader("📊 Resultados del Cálculo Básico")
            
            # Mostrar resultados en columnas
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Peso del Muro", f"{peso_muro:.2f} kN")
                st.metric("Empuje del Suelo", f"{empuje_suelo:.2f} kN")
                st.metric("Volumen", f"{volumen:.2f} m³")
                st.metric("Coeficiente Ka", f"{ka:.3f}")
            
            with col2:
                st.metric("Factor de Seguridad", f"{fs_volcamiento:.2f}")
                st.metric("Momento Volcador", f"{momento_volcador:.2f} kN·m")
                st.metric("Momento Estabilizador", f"{momento_estabilizador:.2f} kN·m")
                st.metric("Altura", f"{altura:.1f} m")
            
            # Análisis de estabilidad
            st.subheader("🔍 Análisis de Estabilidad")
            if fs_volcamiento > 1.5:
                st.success(f"✅ El muro es estable al volcamiento (FS = {fs_volcamiento:.2f} > 1.5)")
            else:
                st.error(f"⚠️ El muro requiere revisión de estabilidad (FS = {fs_volcamiento:.2f} < 1.5)")
            
            # Gráfico básico
            st.subheader("📈 Gráfico de Fuerzas")
            datos = pd.DataFrame({
                'Fuerza': ['Peso Muro', 'Empuje Suelo'],
                'Valor (kN)': [peso_muro, empuje_suelo]
            })
            
            # Gráfico de barras mejorado
            fig = px.bar(datos, x='Fuerza', y='Valor (kN)', 
                        title="Comparación de Fuerzas - Plan Gratuito",
                        color='Fuerza',
                        color_discrete_map={'Peso Muro': '#2E8B57', 'Empuje Suelo': '#DC143C'})
            
            # Personalizar el gráfico
            fig.update_layout(
                xaxis_title="Tipo de Fuerza",
                yaxis_title="Valor (kN)",
                showlegend=True,
                height=400
            )
            
            # Agregar valores en las barras
            fig.update_traces(texttemplate='%{y:.1f}', textposition='outside')
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Gráfico de momentos
            st.subheader("📊 Gráfico de Momentos")
            datos_momentos = pd.DataFrame({
                'Momento': ['Volcador', 'Estabilizador'],
                'Valor (kN·m)': [momento_volcador, momento_estabilizador]
            })
            
            fig2 = px.pie(datos_momentos, values='Valor (kN·m)', names='Momento',
                         title="Distribución de Momentos - Plan Gratuito",
                         color_discrete_map={'Volcador': '#FF6B6B', 'Estabilizador': '#4ECDC4'})
            
            fig2.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig2, use_container_width=True)

    elif opcion == "📊 Análisis Completo":
        if st.session_state['plan'] == "gratuito":
            st.warning("⚠️ Esta función requiere plan premium. Actualiza tu cuenta para acceder a análisis completos.")
            st.info("Plan gratuito incluye: Cálculos básicos, resultados simples")
            st.info("Plan premium incluye: Análisis completo, reportes detallados, gráficos avanzados")
        else:
            st.title("Análisis Completo de Muro de Contención")
            st.success("⭐ Plan Premium: Análisis completo con teoría de Rankine")
            
            # Datos de entrada completos
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Dimensiones")
                h1 = st.number_input("Altura del talud (m)", value=2.8, step=0.1)
                Df = st.number_input("Profundidad de desplante (m)", value=1.2, step=0.1)
                hm = st.number_input("Altura de coronación (m)", value=0.8, step=0.1)
                
                st.subheader("Materiales")
                gamma_relleno = st.number_input("Densidad del relleno (kg/m³)", value=1800, step=50)
                phi_relleno = st.number_input("Ángulo de fricción del relleno (°)", value=30, step=1)
                gamma_concreto = st.number_input("Peso específico del concreto (kg/m³)", value=2400, step=50)
                
            with col2:
                st.subheader("Propiedades del Suelo")
                gamma_cimentacion = st.number_input("Densidad del suelo de cimentación (kg/m³)", value=1700, step=50)
                phi_cimentacion = st.number_input("Ángulo de fricción del suelo (°)", value=25, step=1)
                cohesion = st.number_input("Cohesión del suelo (t/m²)", value=1.0, step=0.1)
                sigma_adm = st.number_input("Capacidad portante del suelo (kg/cm²)", value=2.5, step=0.1)
                
                st.subheader("Cargas")
                qsc = st.number_input("Sobrecarga (kg/m²)", value=1000, step=100)
                fc = st.number_input("Resistencia del concreto (kg/cm²)", value=210, step=10)
                fy = st.number_input("Resistencia del acero (kg/cm²)", value=4200, step=100)
            
            if st.button("🔬 Ejecutar Análisis Completo", type="primary"):
                # Cálculos completos basados en TAREA_DE_PROGRAMACION2.py
                
                # Coeficiente de empuje activo
                phi_relleno_rad = math.radians(phi_relleno)
                ka = (1 - math.sin(phi_relleno_rad)) / (1 + math.sin(phi_relleno_rad))
                
                # Altura equivalente por sobrecarga
                hs = qsc / gamma_relleno
                
                # Factor kc para concreto
                kc = 14.28  # Para fc = 210 kg/cm²
                
                # Dimensiones calculadas
                Bz = (h1 + Df) * (1 + hs/(h1 + Df)) * math.sqrt(ka)
                Bz = round(Bz, 2)
                
                hz = math.sqrt(((h1 + Df)**2 * (1 + hs/(h1 + Df))) / (9 * kc))
                hz = round(hz * 100) / 100
                hz = max(0.4, hz)
                
                b = math.sqrt(((h1 + hm)**2 * (1 + hs/(h1 + hm))) / (10 * kc))
                b = round(b * 100) / 100
                b = max(0.35, b)
                
                r = (2 * Bz - 3 * b) / 6
                r = round(r * 100) / 100
                r = max(0.7, r)
                
                t = Bz - r - b
                t = round(t * 100) / 100
                
                # Cálculos de estabilidad
                # Empuje activo
                Ea = 0.5 * (gamma_relleno/1000) * h1**2 * ka
                
                # Peso del muro
                W_muro = b * h1 * (gamma_concreto/1000)
                W_zapata = Bz * hz * (gamma_concreto/1000)
                W_relleno = t * h1 * (gamma_relleno/1000)
                
                # Momentos
                M_volcador = Ea * h1 / 3
                M_estabilizador = W_muro * (r + b/2) + W_zapata * Bz/2 + W_relleno * (r + b + t/2)
                
                # Factor de seguridad al volcamiento
                FS_volcamiento = M_estabilizador / M_volcador
                
                # Guardar resultados completos
                st.session_state['resultados_completos'] = {
                    'ka': ka,
                    'hs': hs,
                    'Bz': Bz,
                    'hz': hz,
                    'b': b,
                    'r': r,
                    't': t,
                    'Ea': Ea,
                    'W_muro': W_muro,
                    'W_zapata': W_zapata,
                    'W_relleno': W_relleno,
                    'M_volcador': M_volcador,
                    'M_estabilizador': M_estabilizador,
                    'FS_volcamiento': FS_volcamiento
                }
                
                st.success("¡Análisis completo ejecutado exitosamente!")
                st.balloons()
                
                # MOSTRAR RESULTADOS COMPLETOS INMEDIATAMENTE
                st.subheader("📊 Resultados del Análisis Completo")
                
                # Mostrar resultados en columnas
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Coeficiente Ka", f"{ka:.3f}")
                    st.metric("Ancho de Zapata (Bz)", f"{Bz:.2f} m")
                    st.metric("Peralte de Zapata (hz)", f"{hz:.2f} m")
                    st.metric("Espesor del Muro (b)", f"{b:.2f} m")
                    st.metric("Longitud de Puntera (r)", f"{r:.2f} m")
                    st.metric("Longitud de Talón (t)", f"{t:.2f} m")
                
                with col2:
                    st.metric("Empuje Activo (Ea)", f"{Ea:.2f} tn/m")
                    st.metric("Peso del Muro", f"{W_muro:.2f} tn/m")
                    st.metric("Peso de la Zapata", f"{W_zapata:.2f} tn/m")
                    st.metric("Peso del Relleno", f"{W_relleno:.2f} tn/m")
                    st.metric("Factor de Seguridad", f"{FS_volcamiento:.2f}")
                    st.metric("Altura Equivalente (hs)", f"{hs:.3f} m")
                
                # Análisis de estabilidad
                st.subheader("🔍 Análisis de Estabilidad")
                if FS_volcamiento > 2.0:
                    st.success(f"✅ El muro cumple con los requisitos de estabilidad al volcamiento (FS = {FS_volcamiento:.2f} > 2.0)")
                else:
                    st.error(f"⚠️ El muro requiere revisión de dimensiones (FS = {FS_volcamiento:.2f} < 2.0)")

    elif opcion == "📄 Generar Reporte":
        st.title("Generar Reporte Técnico")
        
        if st.session_state['plan'] == "gratuito":
            if 'resultados_basicos' in st.session_state:
                resultados = st.session_state['resultados_basicos']
                
                # Reporte básico gratuito
                reporte_basico = f"""
# REPORTE BÁSICO - MURO DE CONTENCIÓN
## CONSORCIO DEJ
### Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}

### DATOS DE ENTRADA:
- Altura del muro: {resultados['altura']:.2f} m
- Base del muro: {resultados['base']:.2f} m
- Espesor del muro: {resultados['espesor']:.2f} m
- Longitud del muro: {resultados['longitud']:.2f} m
- Peso específico del hormigón: 24.0 kN/m³
- Peso específico del suelo: 18.0 kN/m³
- Ángulo de fricción del suelo: 30.0°

### RESULTADOS DEL CÁLCULO:
- Peso del muro: {resultados['peso_muro']:.2f} kN
- Empuje del suelo: {resultados['empuje_suelo']:.2f} kN
- Factor de seguridad al volcamiento: {resultados['fs_volcamiento']:.2f}
- Volumen de hormigón: {resultados['volumen']:.2f} m³
- Coeficiente de empuje activo (Ka): {resultados['ka']:.3f}
- Momento volcador: {resultados['momento_volcador']:.2f} kN·m
- Momento estabilizador: {resultados['momento_estabilizador']:.2f} kN·m

### ANÁLISIS DE ESTABILIDAD:
"""
                
                if resultados['fs_volcamiento'] > 1.5:
                    reporte_basico += "✅ El muro es estable al volcamiento (FS > 1.5)"
                else:
                    reporte_basico += "⚠️ El muro requiere revisión de estabilidad (FS < 1.5)"
                
                reporte_basico += f"""

### CONCLUSIONES:
El análisis básico indica que el muro de contención {'cumple' if resultados['fs_volcamiento'] > 1.5 else 'no cumple'} con los requisitos mínimos de estabilidad al volcamiento.

### NOTA:
Este es un reporte básico del plan gratuito. Para análisis más detallados, considere actualizar al plan premium.

---
Generado por: CONSORCIO DEJ
Plan: Gratuito
"""
                
                st.text_area("Reporte Básico", reporte_basico, height=500)
                
                st.download_button(
                    label="📥 Descargar Reporte Básico",
                    data=reporte_basico,
                    file_name=f"reporte_basico_muro_contencion_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ No hay resultados disponibles. Realiza primero los cálculos básicos.")
        else:
            # Reporte premium completo
            if 'resultados_completos' in st.session_state:
                resultados = st.session_state['resultados_completos']
                
                reporte_premium = f"""
# REPORTE TÉCNICO COMPLETO - MURO DE CONTENCIÓN
## CONSORCIO DEJ
### Análisis según Teoría de Rankine
### Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}

### 1. COEFICIENTES DE PRESIÓN:
- Coeficiente de empuje activo (Ka): {resultados['ka']:.3f}
- Altura equivalente por sobrecarga (hs): {resultados['hs']:.3f} m

### 2. DIMENSIONES CALCULADAS:
- Ancho de zapata (Bz): {resultados['Bz']:.2f} m
- Peralte de zapata (hz): {resultados['hz']:.2f} m
- Espesor del muro (b): {resultados['b']:.2f} m
- Longitud de puntera (r): {resultados['r']:.2f} m
- Longitud de talón (t): {resultados['t']:.2f} m

### 3. ANÁLISIS DE ESTABILIDAD:
- Empuje activo (Ea): {resultados['Ea']:.2f} tn/m
- Peso del muro: {resultados['W_muro']:.2f} tn/m
- Peso de la zapata: {resultados['W_zapata']:.2f} tn/m
- Peso del relleno: {resultados['W_relleno']:.2f} tn/m

### 4. MOMENTOS:
- Momento volcador: {resultados['M_volcador']:.2f} tn·m/m
- Momento estabilizador: {resultados['M_estabilizador']:.2f} tn·m/m
- Factor de seguridad al volcamiento: {resultados['FS_volcamiento']:.2f}

### 5. VERIFICACIONES:
"""
                
                if resultados['FS_volcamiento'] > 2.0:
                    reporte_premium += "✅ El muro cumple con los requisitos de estabilidad al volcamiento (FS > 2.0)"
                else:
                    reporte_premium += "⚠️ El muro requiere revisión de dimensiones (FS < 2.0)"
                
                reporte_premium += f"""

### 6. CONCLUSIONES:
El análisis completo según la teoría de Rankine indica que el muro de contención {'cumple' if resultados['FS_volcamiento'] > 2.0 else 'no cumple'} con todos los requisitos de estabilidad.

### 7. RECOMENDACIONES:
- Verificar la capacidad portante del suelo
- Revisar el diseño del refuerzo estructural
- Considerar efectos sísmicos si aplica
- Realizar inspecciones periódicas durante la construcción

---
Generado por: CONSORCIO DEJ
Plan: Premium
Método: Teoría de Rankine
"""
                
                st.text_area("Reporte Premium", reporte_premium, height=600)
                
                st.download_button(
                    label="📥 Descargar Reporte Premium",
                    data=reporte_premium,
                    file_name=f"reporte_premium_muro_contencion_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ No hay resultados disponibles. Realiza primero el análisis completo.")

    elif opcion == "📈 Gráficos":
        st.title("Gráficos y Visualizaciones")
        
        if st.session_state['plan'] == "gratuito":
            if 'resultados_basicos' in st.session_state:
                resultados = st.session_state['resultados_basicos']
                
                # Gráfico básico gratuito
                datos = pd.DataFrame({
                    'Fuerza': ['Peso Muro', 'Empuje Suelo'],
                    'Valor (kN)': [resultados['peso_muro'], resultados['empuje_suelo']]
                })
                
                fig = px.bar(datos, x='Fuerza', y='Valor (kN)', 
                            title="Comparación de Fuerzas - Plan Gratuito",
                            color='Fuerza',
                            color_discrete_map={'Peso Muro': '#2E8B57', 'Empuje Suelo': '#DC143C'})
                
                fig.update_layout(
                    xaxis_title="Tipo de Fuerza",
                    yaxis_title="Valor (kN)",
                    height=400
                )
                
                fig.update_traces(texttemplate='%{y:.1f}', textposition='outside')
                st.plotly_chart(fig, use_container_width=True)
                
                # Gráfico de momentos
                datos_momentos = pd.DataFrame({
                    'Momento': ['Volcador', 'Estabilizador'],
                    'Valor (kN·m)': [resultados['momento_volcador'], resultados['momento_estabilizador']]
                })
                
                fig2 = px.pie(datos_momentos, values='Valor (kN·m)', names='Momento',
                             title="Distribución de Momentos - Plan Gratuito",
                             color_discrete_map={'Volcador': '#FF6B6B', 'Estabilizador': '#4ECDC4'})
                
                fig2.update_traces(textposition='inside', textinfo='percent+label+value')
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.warning("⚠️ No hay resultados disponibles. Realiza primero los cálculos básicos.")
        else:
            # Gráficos premium
            if 'resultados_completos' in st.session_state:
                resultados = st.session_state['resultados_completos']
                
                # Gráfico de fuerzas
                col1, col2 = st.columns(2)
                
                with col1:
                    datos_fuerzas = pd.DataFrame({
                        'Fuerza': ['Empuje Activo', 'Peso Muro', 'Peso Zapata', 'Peso Relleno'],
                        'Valor (tn/m)': [resultados['Ea'], resultados['W_muro'], 
                                        resultados['W_zapata'], resultados['W_relleno']]
                    })
                    
                    fig1 = px.bar(datos_fuerzas, x='Fuerza', y='Valor (tn/m)',
                                 title="Análisis de Fuerzas - Plan Premium",
                                 color='Fuerza',
                                 color_discrete_map={
                                     'Empuje Activo': '#DC143C',
                                     'Peso Muro': '#2E8B57',
                                     'Peso Zapata': '#4169E1',
                                     'Peso Relleno': '#FF8C00'
                                 })
                    
                    fig1.update_layout(
                        xaxis_title="Tipo de Fuerza",
                        yaxis_title="Valor (tn/m)",
                        height=400
                    )
                    
                    fig1.update_traces(texttemplate='%{y:.2f}', textposition='outside')
                    st.plotly_chart(fig1, use_container_width=True)
                
                with col2:
                    # Gráfico de momentos
                    datos_momentos = pd.DataFrame({
                        'Momento': ['Volcador', 'Estabilizador'],
                        'Valor (tn·m/m)': [resultados['M_volcador'], resultados['M_estabilizador']]
                    })
                    
                    fig2 = px.pie(datos_momentos, values='Valor (tn·m/m)', names='Momento',
                                 title="Distribución de Momentos - Plan Premium",
                                 color_discrete_map={'Volcador': '#FF6B6B', 'Estabilizador': '#4ECDC4'})
                    
                    fig2.update_traces(textposition='inside', textinfo='percent+label+value')
                    st.plotly_chart(fig2, use_container_width=True)
                
                # Gráfico de dimensiones
                st.subheader("📏 Dimensiones del Muro")
                dimensiones = {
                    'Dimensión': ['Bz', 'hz', 'b', 'r', 't'],
                    'Valor (m)': [resultados['Bz'], resultados['hz'], resultados['b'], 
                                 resultados['r'], resultados['t']]
                }
                
                fig3 = px.bar(pd.DataFrame(dimensiones), x='Dimensión', y='Valor (m)',
                             title="Dimensiones Calculadas del Muro - Plan Premium",
                             color='Dimensión',
                             color_discrete_map={
                                 'Bz': '#FF1493',
                                 'hz': '#00CED1',
                                 'b': '#32CD32',
                                 'r': '#FFD700',
                                 't': '#FF6347'
                             })
                
                fig3.update_layout(
                    xaxis_title="Dimensión",
                    yaxis_title="Valor (m)",
                    height=400
                )
                
                fig3.update_traces(texttemplate='%{y:.2f}', textposition='outside')
                st.plotly_chart(fig3, use_container_width=True)
            else:
                st.warning("⚠️ No hay resultados disponibles. Realiza primero el análisis completo.")

    elif opcion == "ℹ️ Acerca de":
        st.title("Acerca de CONSORCIO DEJ")
        st.write("""
        ### 🏗️ CONSORCIO DEJ
        **Ingeniería y Construcción Especializada**
        
        Esta aplicación fue desarrollada para facilitar el cálculo y diseño de muros de contención
        utilizando métodos reconocidos en ingeniería geotécnica.
        
        **Características del Plan Gratuito:**
        - ✅ Cálculos básicos de estabilidad
        - ✅ Resultados simples con gráficos
        - ✅ Reporte básico descargable
        - ✅ Análisis de factor de seguridad
        
        **Características del Plan Premium:**
        - ⭐ Análisis completo con teoría de Rankine
        - ⭐ Cálculos de dimensiones automáticos
        - ⭐ Reportes técnicos detallados
        - ⭐ Gráficos avanzados y visualizaciones
        - ⭐ Verificaciones de estabilidad completas
        
        **Desarrollado con:** Python, Streamlit, Plotly
        **Normativas:** Aplicación de la teoría de Rankine para muros de contención
        """)

    elif opcion == "✉️ Contacto":
        st.title("Contacto")
        st.write("""
        ### 🏗️ CONSORCIO DEJ
        **Información de Contacto:**
        
        📧 Email: dejconstruct@gmail.com  
        📱 Teléfono: +51 967573364  
        🌐 Web: www.gruposelectiva.com  
        📍 Dirección: [Jose Luis Bustamante Rivero - Arequipa]
        
        **Horarios de Atención:**
        Lunes a Viernes: 8:00 AM - 6:00 PM
        
        **Servicios:**
        - Diseño de muros de contención
        - Análisis geotécnico
        - Ingeniería estructural
        - Construcción especializada
        """)

    # Mostrar plan actual en sidebar
    if st.session_state['plan'] == "gratuito":
        st.sidebar.info("🆓 Plan Gratuito - Funciones limitadas")
        st.sidebar.write("Para acceder a todas las funciones, actualiza a Premium")
        
        # Información sobre cómo acceder al plan premium
        st.sidebar.markdown("---")
        st.sidebar.subheader("🔑 Acceso Premium")
        st.sidebar.write("**Usuario:** premium")
        st.sidebar.write("**Contraseña:** premium")
        st.sidebar.info("Cierra sesión y vuelve a iniciar con las credenciales premium")
    else:
        st.sidebar.success("⭐ Plan Premium - Acceso completo")
        
        # Información para administradores
        st.sidebar.markdown("---")
        st.sidebar.subheader("👨‍💼 Panel de Administrador")
        st.sidebar.write("**Usuario actual:** " + st.session_state['user'])
        st.sidebar.write("**Plan:** Premium")
        st.sidebar.success("Acceso completo a todas las funciones")
