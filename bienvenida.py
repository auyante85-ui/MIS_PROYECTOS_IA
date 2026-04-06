import streamlit as st

# Configuración de la página (esto pone el icono en la pestaña del navegador)
st.set_page_config(page_title="Consultoría IA", page_icon="🤖")

# Título profesional con icono
st.markdown("<h1 style='text-align: center;'>🏢 Bienvenida al Mundo de la IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Transformando empresas con tecnología inteligente</p>", unsafe_allow_html=True)

st.divider() # Una línea elegante para separar

# Imagen profesional de tecnología al principio
st.image(
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1600&q=80",
    caption="Tecnología aplicada para impulsar tu negocio",
    use_container_width=True,
)s

# Creamos 3 columnas para que los formularios queden alineados
col1, col2, col3 = st.columns(3)

with col1:
    nombre = st.text_input("👤 Tu Nombre", placeholder="Ej: Yvett")

with col2:
    empresa = st.text_input("🏢 Empresa", placeholder="Ej: Innova IA")

with col3:
    sector = st.text_input("📂 Sector", placeholder="Ej: Recursos Humanos")

# Botón centrado y estilizado
st.write("---")
if st.button("🚀 Registrar y Generar Consejo", use_container_width=True):
    if nombre and empresa and sector:
        # Mensaje de éxito dentro de un cuadro elegante
        st.info(f"¡Genial {nombre}! Hemos registrado a **{empresa}** correctamente.")
        
        # Caja de consejo profesional
        with st.container():
            st.info(f"💡 **Consejo de IA para {sector}:** La automatización de procesos en este sector puede reducir tus tareas repetitivas en un 40%. ¡Es el momento de empezar!")
    else:
        st.warning("⚠️ Por favor, completa todos los campos para continuar.")

# Botón de globos al final
st.divider()
if st.button("🎈 Activar globos"):
    st.balloons()
        