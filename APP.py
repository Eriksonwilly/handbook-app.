import streamlit as st

st.image("LOGO CONTRUCtora dej6.png", width=200)  # Ajusta el nombre y tamaño según tu archivo

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
    # Aquí va tu lógica de muro de contención (puedo ayudarte a migrarla)
    st.write("Aquí va la app principal...")

    # Modo gratis vs pago (ejemplo)
    if st.session_state['user'] == "demo":
        st.info("Estás en modo gratis. Para más funciones, suscríbete.")
    else:
        st.success("Modo premium activado.")
