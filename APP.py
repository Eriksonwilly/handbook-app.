import streamlit as st
import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

# Función para dibujar el muro de contención
def dibujar_muro_streamlit(dimensiones, h1, Df, qsc):
    """
    Dibuja el muro de contención con las dimensiones calculadas para Streamlit.
    
    Parámetros:
    -----------
    dimensiones : dict
        Diccionario con las dimensiones calculadas del muro
    h1 : float
        Altura del talud (m)
    Df : float
        Profundidad de desplante (m)
    qsc : float
        Sobrecarga (kg/m²)
    
    Retorna:
    --------
    matplotlib.figure.Figure
        Figura con el dibujo del muro
    """
    # Configurar estilo profesional
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Extraer dimensiones
    Bz = dimensiones['Bz']
    hz = dimensiones['hz']
    b = dimensiones['b']
    r = dimensiones['r']
    t = dimensiones['t']
    hm = dimensiones['hm']
    
    # Colores profesionales mejorados
    color_zapata = '#4FC3F7'  # Azul claro profesional
    color_muro = '#FF5722'    # Naranja vibrante
    color_relleno = '#FFC107' # Amarillo dorado
    color_suelo = '#8D6E63'   # Marrón tierra
    color_agua = '#81C784'    # Verde agua
    color_acero = '#607D8B'   # Gris acero
    
    # Dibujar suelo de cimentación con gradiente
    suelo_gradient = np.linspace(0.3, 0.8, 50)
    for i, alpha in enumerate(suelo_gradient):
        y_pos = -Df + (i * Df / 50)
        ax.add_patch(Rectangle((-1, y_pos), Bz+2, Df/50, 
                              facecolor=color_suelo, edgecolor='none', alpha=alpha))
    
    # Dibujar zapata con efecto 3D
    ax.add_patch(Rectangle((0, 0), Bz, hz, facecolor=color_zapata, 
                          edgecolor='#1565C0', linewidth=3))
    
    # Dibujar muro principal con gradiente
    for i in range(10):
        alpha = 0.7 + (i * 0.03)
        ax.add_patch(Rectangle((r, hz + i*h1/10), b, h1/10, 
                              facecolor=color_muro, edgecolor='#D84315', 
                              linewidth=1, alpha=alpha))
    
    # Dibujar parte superior del muro
    ax.add_patch(Rectangle((r, hz + h1), b, hm, facecolor=color_muro, 
                          edgecolor='#D84315', linewidth=3))
    
    # Dibujar relleno con patrón
    relleno_pts = [(r+b, hz), (Bz, hz), (Bz, hz+h1+hm), (r+b, hz+h1+hm)]
    ax.add_patch(Polygon(relleno_pts, facecolor=color_relleno, 
                        edgecolor='#F57F17', linewidth=2, alpha=0.8))
    
    # Agregar patrón de relleno (puntos)
    for i in range(20):
        x = r + b + (i * t / 20) + np.random.normal(0, 0.02)
        y = hz + np.random.uniform(0, h1+hm)
        if x < Bz and y < hz+h1+hm:
            ax.scatter(x, y, c='#F57F17', s=15, alpha=0.6)
    
    # Dibujar sobrecarga con flechas mejoradas y profesionales
    flechas_x = np.linspace(r+b+0.1, Bz-0.1, 15)
    for i, x in enumerate(flechas_x):
        color_flecha = '#D32F2F' if i % 3 == 0 else '#F44336' if i % 3 == 1 else '#E53935'
        ax.arrow(x, hz+h1+hm+0.7, 0, -0.5, head_width=0.1, head_length=0.2, 
                fc=color_flecha, ec=color_flecha, linewidth=4, alpha=0.9)
    
    # Texto de sobrecarga con fondo profesional
    ax.text(Bz/2, hz+h1+hm+1.0, f'SOBRECARGA APLICADA: {qsc} kg/m²', 
            ha='center', fontsize=16, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.5", facecolor='#FFEBEE', 
                     edgecolor='#D32F2F', linewidth=3, alpha=0.95))
    
    # Agregar línea de nivel del terreno
    ax.axhline(y=hz, color='#795548', linewidth=3, linestyle='-', alpha=0.8)
    ax.text(Bz+0.3, hz, 'NIVEL DEL TERRENO', fontsize=12, fontweight='bold', 
            color='#795548', rotation=90, va='center')
    
    # Añadir dimensiones con estilo profesional
    dimension_style = dict(arrowstyle='<->', color='#1976D2', linewidth=3)
    
    # Dimensiones horizontales
    ax.annotate('', xy=(0, hz/2), xytext=(r, hz/2), arrowprops=dimension_style)
    ax.text(r/2, hz/2-0.15, f'r = {r}m', ha='center', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(r, hz/2), xytext=(r+b, hz/2), arrowprops=dimension_style)
    ax.text(r+b/2, hz/2-0.15, f'b = {b}m', ha='center', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(r+b, hz/2), xytext=(Bz, hz/2), arrowprops=dimension_style)
    ax.text(r+b+t/2, hz/2-0.15, f't = {t}m', ha='center', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    # Dimensiones verticales
    ax.annotate('', xy=(r+b/2, hz), xytext=(r+b/2, hz+h1), arrowprops=dimension_style)
    ax.text(r+b/2-0.2, hz+h1/2, f'h1 = {h1}m', ha='right', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(r+b/2, hz+h1), xytext=(r+b/2, hz+h1+hm), arrowprops=dimension_style)
    ax.text(r+b/2-0.2, hz+h1+hm/2, f'hm = {hm}m', ha='right', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(r+b/2, 0), xytext=(r+b/2, -Df), arrowprops=dimension_style)
    ax.text(r+b/2-0.2, -Df/2, f'Df = {Df}m', ha='right', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(0, 0), xytext=(0, hz), arrowprops=dimension_style)
    ax.text(-0.2, hz/2, f'hz = {hz}m', ha='right', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    ax.annotate('', xy=(0, 0), xytext=(Bz, 0), arrowprops=dimension_style)
    ax.text(Bz/2, -0.3, f'Bz = {Bz}m', ha='center', fontsize=11, fontweight='bold', 
            color='#1976D2', bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                      edgecolor='#1976D2', alpha=0.9))
    
    # Ajustar límites del gráfico
    ax.set_xlim(-1.5, Bz+1.5)
    ax.set_ylim(-Df-0.8, hz+h1+hm+1.2)
    
    # Configurar aspecto y títulos profesionales
    ax.set_aspect('equal')
    ax.set_title('DISEÑO PROFESIONAL DE MURO DE CONTENCIÓN\nCONSORCIO DEJ - Ingeniería y Construcción', 
                fontsize=18, fontweight='bold', pad=30, color='#1565C0')
    ax.set_xlabel('Distancia (metros)', fontsize=14, fontweight='bold', color='#424242')
    ax.set_ylabel('Altura (metros)', fontsize=14, fontweight='bold', color='#424242')
    
    # Agregar leyenda profesional
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=color_zapata, edgecolor='#1565C0', label='ZAPATA DE CIMENTACIÓN'),
        Patch(facecolor=color_muro, edgecolor='#D84315', label='MURO DE CONTENCIÓN'),
        Patch(facecolor=color_relleno, edgecolor='#F57F17', label='MATERIAL DE RELLENO'),
        Patch(facecolor=color_suelo, edgecolor='#5D4037', label='SUELO DE CIMENTACIÓN')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12, 
             frameon=True, fancybox=True, shadow=True, 
             title='ELEMENTOS ESTRUCTURALES', title_fontsize=13)
    
    # Agregar grid sutil
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # Configurar fondo
    ax.set_facecolor('#FAFAFA')
    fig.patch.set_facecolor('white')
    
    plt.tight_layout()
    return fig

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
                
                # Coeficiente de empuje activo (fórmula correcta de Rankine)
                phi_relleno_rad = math.radians(phi_relleno)
                ka = math.tan(math.radians(45 - phi_relleno/2))**2
                
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
                
                # Cálculos de estabilidad completos (basados en AVANCE2.PY)
                
                # 1. Empujes activos
                Ea_relleno = 0.5 * ka * (gamma_relleno/1000) * h1**2
                Ea_sobrecarga = ka * (qsc/1000) * h1  # Convertir kg/m² a tn/m²
                Ea_total = Ea_relleno + Ea_sobrecarga
                
                # 2. Empuje pasivo (si aplica)
                phi_cimentacion_rad = math.radians(phi_cimentacion)
                kp = math.tan(math.radians(45 + phi_cimentacion/2))**2
                Ep = 0.5 * kp * (gamma_cimentacion/1000) * Df**2
                
                # 3. Pesos de cada elemento
                W_muro = b * h1 * (gamma_concreto/1000)
                W_zapata = Bz * hz * (gamma_concreto/1000)
                W_relleno = t * h1 * (gamma_relleno/1000)
                
                # 4. Posiciones de los pesos (brazos de momento)
                x_muro = r + b/2
                x_zapata = Bz/2
                x_relleno = r + b + t/2
                
                # 5. Momentos estabilizadores
                Mr_muro = W_muro * x_muro
                Mr_zapata = W_zapata * x_zapata
                Mr_relleno = W_relleno * x_relleno
                Mr_pasivo = Ep * Df/3
                M_estabilizador = Mr_muro + Mr_zapata + Mr_relleno + Mr_pasivo
                
                # 6. Momentos volcadores
                Mv_relleno = Ea_relleno * h1/3
                Mv_sobrecarga = Ea_sobrecarga * h1/2
                M_volcador = Mv_relleno + Mv_sobrecarga
                
                # 7. Factor de seguridad al volcamiento
                FS_volcamiento = M_estabilizador / M_volcador
                
                # 8. Verificación al deslizamiento
                mu = math.tan(phi_cimentacion_rad)  # Coeficiente de fricción
                Fr_friccion = mu * (W_muro + W_zapata + W_relleno)
                Fr_pasivo = Ep
                Fr_total = Fr_friccion + Fr_pasivo
                Fd_total = Ea_total
                FS_deslizamiento = Fr_total / Fd_total
                
                # 9. Verificación de presiones sobre el suelo
                W_total = W_muro + W_zapata + W_relleno
                
                # Posición de la resultante vertical
                sum_momentos_verticales = Mr_muro + Mr_zapata + Mr_relleno
                x_barra = sum_momentos_verticales / W_total
                
                # Excentricidad
                e = abs(x_barra - Bz/2)
                
                # Presiones máxima y mínima
                q_max = (W_total / Bz) * (1 + 6*e/Bz)
                q_min = (W_total / Bz) * (1 - 6*e/Bz)
                
                # Verificar si hay tensiones
                tension = q_min < 0
                
                # Convertir a kg/cm²
                q_max_kg_cm2 = q_max * 0.1  # tn/m² a kg/cm²
                q_min_kg_cm2 = q_min * 0.1
                
                # Guardar resultados completos
                st.session_state['resultados_completos'] = {
                    'ka': ka,
                    'kp': kp,
                    'hs': hs,
                    'Bz': Bz,
                    'hz': hz,
                    'b': b,
                    'r': r,
                    't': t,
                    'hm': hm,
                    'h1': h1,
                    'Df': Df,
                    'qsc': qsc,
                    'Ea_relleno': Ea_relleno,
                    'Ea_sobrecarga': Ea_sobrecarga,
                    'Ea_total': Ea_total,
                    'Ep': Ep,
                    'W_muro': W_muro,
                    'W_zapata': W_zapata,
                    'W_relleno': W_relleno,
                    'W_total': W_total,
                    'M_volcador': M_volcador,
                    'M_estabilizador': M_estabilizador,
                    'FS_volcamiento': FS_volcamiento,
                    'FS_deslizamiento': FS_deslizamiento,
                    'q_max_kg_cm2': q_max_kg_cm2,
                    'q_min_kg_cm2': q_min_kg_cm2,
                    'e': e,
                    'tension': tension
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
                    st.metric("Empuje Activo Total", f"{Ea_total:.2f} tn/m")
                    st.metric("Empuje Pasivo", f"{Ep:.2f} tn/m")
                    st.metric("Peso Total", f"{W_total:.2f} tn/m")
                    st.metric("FS Deslizamiento", f"{FS_deslizamiento:.2f}")
                    st.metric("Presión Máxima", f"{q_max_kg_cm2:.2f} kg/cm²")
                    st.metric("Excentricidad", f"{e:.3f} m")
                
                # Análisis de estabilidad completo
                st.subheader("🔍 Análisis de Estabilidad Completo")
                
                # Verificación al volcamiento
                col1, col2 = st.columns(2)
                with col1:
                    if FS_volcamiento >= 2.0:
                        st.success(f"✅ **Volcamiento:** CUMPLE (FS = {FS_volcamiento:.2f} ≥ 2.0)")
                    else:
                        st.error(f"⚠️ **Volcamiento:** NO CUMPLE (FS = {FS_volcamiento:.2f} < 2.0)")
                
                with col2:
                    if FS_deslizamiento >= 1.5:
                        st.success(f"✅ **Deslizamiento:** CUMPLE (FS = {FS_deslizamiento:.2f} ≥ 1.5)")
                    else:
                        st.error(f"⚠️ **Deslizamiento:** NO CUMPLE (FS = {FS_deslizamiento:.2f} < 1.5)")
                
                # Verificación de presiones
                st.subheader("📊 Verificación de Presiones sobre el Suelo")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Presión Máxima", f"{q_max_kg_cm2:.2f} kg/cm²")
                    if q_max_kg_cm2 <= sigma_adm:
                        st.success(f"✅ ≤ {sigma_adm} kg/cm²")
                    else:
                        st.error(f"⚠️ > {sigma_adm} kg/cm²")
                
                with col2:
                    st.metric("Presión Mínima", f"{q_min_kg_cm2:.2f} kg/cm²")
                    if not tension:
                        st.success("✅ Sin tensiones")
                    else:
                        st.error("⚠️ Hay tensiones")
                
                with col3:
                    st.metric("Excentricidad", f"{e:.3f} m")
                    e_limite = Bz / 6
                    if e <= e_limite:
                        st.success(f"✅ ≤ B/6 ({e_limite:.3f} m)")
                    else:
                        st.error(f"⚠️ > B/6 ({e_limite:.3f} m)")
                
                # Resumen final
                cumple_todo = (FS_volcamiento >= 2.0 and FS_deslizamiento >= 1.5 and 
                              q_max_kg_cm2 <= sigma_adm and not tension and e <= e_limite)
                
                if cumple_todo:
                    st.success("🎉 **RESULTADO FINAL:** El muro CUMPLE con todos los requisitos de estabilidad")
                else:
                    st.error("⚠️ **RESULTADO FINAL:** El muro NO CUMPLE con todos los requisitos. Se recomienda revisar dimensiones.")
                
                # Gráfico del muro de contención
                st.subheader("🏗️ Visualización del Muro de Contención")
                st.info("Gráfico detallado del muro con todas las dimensiones calculadas")
                
                # Crear dimensiones para el gráfico
                dimensiones_grafico = {
                    'Bz': Bz,
                    'hz': hz,
                    'b': b,
                    'r': r,
                    't': t,
                    'hm': hm
                }
                
                # Generar el gráfico del muro
                fig_muro = dibujar_muro_streamlit(dimensiones_grafico, h1, Df, qsc)
                
                # Mostrar el gráfico en Streamlit
                st.pyplot(fig_muro)
                
                # Información adicional sobre el gráfico
                st.markdown("""
                **Leyenda del Gráfico:**
                - 🔵 **Zapata (Azul claro):** Base de cimentación del muro
                - 🔴 **Muro (Rosa):** Estructura principal de contención
                - 🟡 **Relleno (Amarillo):** Material de relleno detrás del muro
                - 🟤 **Suelo (Marrón):** Suelo de cimentación
                - 🔴 **Flechas rojas:** Sobrecarga aplicada (qsc)
                - 🔵 **Dimensiones en azul:** Medidas calculadas del muro
                """)

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
                
                # Botones para el reporte básico
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        label="📥 Descargar Reporte Básico",
                        data=reporte_basico,
                        file_name=f"reporte_basico_muro_contencion_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    if st.button("🖨️ Generar Reporte en Pantalla", type="primary"):
                        st.success("✅ Reporte básico generado exitosamente")
                        st.balloons()
                        
                        # Mostrar el reporte en formato expandible
                        with st.expander("📋 VER REPORTE BÁSICO COMPLETO", expanded=True):
                            st.markdown(reporte_basico)
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
- Coeficiente de empuje pasivo (Kp): {resultados['kp']:.3f}
- Altura equivalente por sobrecarga (hs): {resultados['hs']:.3f} m

### 2. DIMENSIONES CALCULADAS:
- Ancho de zapata (Bz): {resultados['Bz']:.2f} m
- Peralte de zapata (hz): {resultados['hz']:.2f} m
- Espesor del muro (b): {resultados['b']:.2f} m
- Longitud de puntera (r): {resultados['r']:.2f} m
- Longitud de talón (t): {resultados['t']:.2f} m
- Altura del talud (h1): {resultados['h1']:.2f} m
- Profundidad de desplante (Df): {resultados['Df']:.2f} m

### 3. ANÁLISIS DE EMPUJES:
- Empuje activo por relleno: {resultados['Ea_relleno']:.2f} tn/m
- Empuje activo por sobrecarga: {resultados['Ea_sobrecarga']:.2f} tn/m
- Empuje activo total: {resultados['Ea_total']:.2f} tn/m
- Empuje pasivo: {resultados['Ep']:.2f} tn/m

### 4. ANÁLISIS DE PESOS:
- Peso del muro: {resultados['W_muro']:.2f} tn/m
- Peso de la zapata: {resultados['W_zapata']:.2f} tn/m
- Peso del relleno: {resultados['W_relleno']:.2f} tn/m
- Peso total: {resultados['W_total']:.2f} tn/m

### 5. MOMENTOS Y FACTORES DE SEGURIDAD:
- Momento volcador: {resultados['M_volcador']:.2f} tn·m/m
- Momento estabilizador: {resultados['M_estabilizador']:.2f} tn·m/m
- Factor de seguridad al volcamiento: {resultados['FS_volcamiento']:.2f}
- Factor de seguridad al deslizamiento: {resultados['FS_deslizamiento']:.2f}

### 6. VERIFICACIÓN DE PRESIONES:
- Presión máxima: {resultados['q_max_kg_cm2']:.2f} kg/cm²
- Presión mínima: {resultados['q_min_kg_cm2']:.2f} kg/cm²
- Excentricidad: {resultados['e']:.3f} m
- Hay tensiones: {'Sí' if resultados['tension'] else 'No'}

### 7. VERIFICACIONES DE ESTABILIDAD:
"""
                
                # Verificaciones de estabilidad
                cumple_volcamiento = resultados['FS_volcamiento'] >= 2.0
                cumple_deslizamiento = resultados['FS_deslizamiento'] >= 1.5
                cumple_presion = resultados['q_max_kg_cm2'] <= 2.5  # Asumiendo q_adm = 2.5 kg/cm²
                cumple_excentricidad = resultados['e'] <= resultados['Bz'] / 6
                sin_tensiones = not resultados['tension']
                
                reporte_premium += f"""
**Verificación al Volcamiento:**
- Factor de seguridad calculado: {resultados['FS_volcamiento']:.2f}
- Factor mínimo requerido: 2.0
- Estado: {'✅ CUMPLE' if cumple_volcamiento else '⚠️ NO CUMPLE'}

**Verificación al Deslizamiento:**
- Factor de seguridad calculado: {resultados['FS_deslizamiento']:.2f}
- Factor mínimo requerido: 1.5
- Estado: {'✅ CUMPLE' if cumple_deslizamiento else '⚠️ NO CUMPLE'}

**Verificación de Presiones:**
- Presión máxima: {resultados['q_max_kg_cm2']:.2f} kg/cm²
- Presión admisible: 2.5 kg/cm²
- Estado: {'✅ CUMPLE' if cumple_presion else '⚠️ NO CUMPLE'}

**Verificación de Excentricidad:**
- Excentricidad calculada: {resultados['e']:.3f} m
- Límite (B/6): {resultados['Bz']/6:.3f} m
- Estado: {'✅ CUMPLE' if cumple_excentricidad else '⚠️ NO CUMPLE'}

**Verificación de Tensiones:**
- Hay tensiones: {'Sí' if resultados['tension'] else 'No'}
- Estado: {'✅ CUMPLE' if sin_tensiones else '⚠️ NO CUMPLE'}

### 8. RESULTADO FINAL:
"""
                
                cumple_todo = cumple_volcamiento and cumple_deslizamiento and cumple_presion and cumple_excentricidad and sin_tensiones
                
                if cumple_todo:
                    reporte_premium += """
🎉 **EL MURO CUMPLE CON TODOS LOS REQUISITOS DE ESTABILIDAD**

El análisis completo según la teoría de Rankine indica que el muro de contención 
es estructuralmente seguro y cumple con todas las verificaciones requeridas.
"""
                else:
                    reporte_premium += """
⚠️ **EL MURO NO CUMPLE CON TODOS LOS REQUISITOS**

Se recomienda revisar las dimensiones del muro o las propiedades del suelo 
para mejorar los factores de seguridad y cumplir con las especificaciones.
"""

                reporte_premium += f"""

### 9. RECOMENDACIONES TÉCNICAS:
- Verificar la capacidad portante del suelo en campo
- Revisar el diseño del refuerzo estructural según ACI 318
- Considerar efectos sísmicos según la normativa local
- Realizar inspecciones periódicas durante la construcción
- Monitorear deformaciones durante el servicio
- Verificar drenaje del relleno para evitar presiones hidrostáticas

### 10. INFORMACIÓN DEL PROYECTO:
- Empresa: CONSORCIO DEJ
- Método de análisis: Teoría de Rankine
- Fecha de análisis: {datetime.now().strftime('%d/%m/%Y %H:%M')}
- Plan: Premium
- Software: Streamlit + Python

---
**Este reporte fue generado automáticamente por el sistema de análisis de muros de contención de CONSORCIO DEJ.**
**Para consultas técnicas, contacte a nuestro equipo de ingeniería.**
"""
                
                st.text_area("Reporte Premium", reporte_premium, height=600)
                
                # Botones para el reporte
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        label="📥 Descargar Reporte Premium",
                        data=reporte_premium,
                        file_name=f"reporte_premium_muro_contencion_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    if st.button("🖨️ Generar Reporte en Pantalla", type="primary"):
                        st.success("✅ Reporte técnico generado exitosamente")
                        st.balloons()
                        
                        # Mostrar el reporte en formato expandible
                        with st.expander("📋 VER REPORTE TÉCNICO COMPLETO", expanded=True):
                            st.markdown(reporte_premium)
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
                        'Fuerza': ['Empuje Activo', 'Empuje Pasivo', 'Peso Total'],
                        'Valor (tn/m)': [resultados['Ea_total'], resultados['Ep'], 
                                        resultados['W_total']]
                    })
                    
                    fig1 = px.bar(datos_fuerzas, x='Fuerza', y='Valor (tn/m)',
                                 title="Análisis de Fuerzas - Plan Premium",
                                 color='Fuerza',
                                 color_discrete_map={
                                     'Empuje Activo': '#DC143C',
                                     'Empuje Pasivo': '#2E8B57',
                                     'Peso Total': '#4169E1'
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
                
                # Gráfico del muro de contención
                st.subheader("🏗️ Visualización del Muro de Contención")
                st.info("Representación gráfica detallada del muro diseñado")
                
                # Crear dimensiones para el gráfico
                dimensiones_grafico = {
                    'Bz': resultados['Bz'],
                    'hz': resultados['hz'],
                    'b': resultados['b'],
                    'r': resultados['r'],
                    't': resultados['t'],
                    'hm': resultados['hm']
                }
                
                # Generar el gráfico del muro con valores reales
                fig_muro = dibujar_muro_streamlit(dimensiones_grafico, resultados['h1'], resultados['Df'], resultados['qsc'])
                
                # Mostrar el gráfico en Streamlit
                st.pyplot(fig_muro)
                
                # Información adicional sobre el gráfico
                st.markdown("""
                **Leyenda del Gráfico:**
                - 🔵 **Zapata (Azul claro):** Base de cimentación del muro
                - 🔴 **Muro (Rosa):** Estructura principal de contención
                - 🟡 **Relleno (Amarillo):** Material de relleno detrás del muro
                - 🟤 **Suelo (Marrón):** Suelo de cimentación
                - 🔴 **Flechas rojas:** Sobrecarga aplicada (qsc)
                - 🔵 **Dimensiones en azul:** Medidas calculadas del muro
                """)
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
        
        📧 Email: contacto@consorciodej.com  
        📱 Teléfono: +123 456 7890  
        🌐 Web: www.consorciodej.com  
        📍 Dirección: [Tu dirección aquí]
        
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