import streamlit as st
from PIL import Image
import base64

# Configuración de la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Función para cargar la imagen y convertirla a base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Ruta de la imagen
image_path = "assets/imagen.png"  # Asegúrate de que esta ruta sea correcta

# Obtener la imagen en base64
image_base64 = get_image_as_base64(image_path)

# Configuración inicial para la navegación
if "page" not in st.session_state:
    st.session_state.page = "inicio"  # Página inicial

# Página de inicio
if st.session_state.page == "inicio":
    st.markdown(
        f"""
        <style>
        .background {{
            position: relative;
            text-align: center;
        }}
        .background img {{
            width: 100%;
            height: auto;
        }}
        .button-overlay {{
            position: absolute;
            bottom: 50px; /* Ajusta esta distancia desde el fondo */
            left: 50%;
            transform: translateX(-50%);
        }}
        .button-overlay button {{
            padding: 15px 32px;
            font-size: 16px;
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
        }}
        .button-overlay button:hover {{
            background-color: #45a049;
        }}
        </style>

        <div class="background">
            <img src="data:image/png;base64,{image_base64}" alt="Background">
            <div class="button-overlay">
                <a href="#" onclick="window.location.reload()">
                    <button>Continuar</button>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Acción de continuar
    if st.button("Continuar"):
        st.session_state.page = "pagina_con_botones"

# Página con los tres botones
elif st.session_state.page == "pagina_con_botones":
    st.title("Página con 3 Botones")

    st.button("Botón 1")
    st.button("Botón 2")
    st.button("Botón 3")

    # Opción para volver a la página inicial
    if st.button("Volver al inicio"):
        st.session_state.page = "inicio"

        
