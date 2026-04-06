import streamlit as st

# 1. Configuración
st.set_page_config(page_title="Consultoría IA", page_icon="🤖")

# 2. Título e Imagen
st.title("🚀 Bienvenido al Mundo de la IA")
st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=1000")

st.divider()

# 3. Formulario
nombre = st.text_input("Tu Nombre")
empresa = st.text_input("Tu Empresa")

if st.button("¡Registrar y ver Magia!"):
    if nombre and empresa:
        st.info(f"✨ ¡Hola {nombre}! Estrategia lista para {empresa}.")
        st.balloons() # <--- ¡AQUÍ ESTÁN LOS GLOBOS!
    else:
        st.warning("Por favor, rellena los campos.")