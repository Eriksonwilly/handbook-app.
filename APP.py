import streamlit as st

col1, col2 = st.columns([1, 3])
with col1:
    st.image("imagenes/LOGO CONSTRUCTORA DEJ6.png", width=100)
with col2:
    st.title("CONSORCIO DEJ")
st.markdown("---")

# Autenticación simple (ejemplo)
def login():
    st.title("Iniciar Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if username == "demo" and password == "demo":
            st.session_state['logged_in'] = True
            st.session_state['user'] = username
        else:
            st.error("Usuario o contraseña incorrectos")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    st.success(f"Bienvenido, {st.session_state['user']}!")
    st.title("Cálculo de Muro de Contención")

    # Entradas del usuario
    altura = st.number_input("Altura del muro (m)", min_value=1.0, max_value=10.0, value=3.0)
    base = st.number_input("Base del muro (m)", min_value=0.5, max_value=5.0, value=1.0)
    peso_especifico = st.number_input("Peso específico del material (kN/m³)", min_value=10.0, max_value=30.0, value=24.0)

    if st.button("Calcular"):
        volumen = altura * base * 1  # Suponiendo 1 metro de longitud
        peso = volumen * peso_especifico
        st.success(f"El peso del muro es: {peso:.2f} kN")

    # Modo gratis vs pago (ejemplo)
    if st.session_state['user'] == "demo":
        st.info("Estás en modo gratis. Para más funciones, suscríbete.")
    else:
        st.success("Modo premium activado.")

st.info("Introduce los datos del muro de contención para calcular su peso aproximado.")

st.sidebar.title("Menú")
opcion = st.sidebar.selectbox("Selecciona una opción", ["Cálculo de muro", "Acerca de", "Contacto"])

if opcion == "Cálculo de muro":
    # Aquí va el código del cálculo
    pass
elif opcion == "Acerca de":
    st.write("Esta app fue desarrollada por Consorcio DEJ.")
elif opcion == "Contacto":
    st.write("Email: contacto@consorciodej.com")
