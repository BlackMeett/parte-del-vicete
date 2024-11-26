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

# Función principal que maneja las páginas
def main():
    # Verificar el estado de la página
    if "page" not in st.session_state:
        st.session_state.page = "inicio"

    # Mostrar las páginas dependiendo del estado
    if st.session_state.page == "inicio":
        show_home_page()
    elif st.session_state.page == "pagina2":
        show_page2()
    elif st.session_state.page == "pagina3":
        show_page3()
    elif st.session_state.page == "pagina4":
        show_page4()

# Página de inicio con el fondo y el botón
def show_home_page():
    st.title("Página de Inicio")
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
                <button onClick="window.location.href = '#';">Continuar</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Al hacer clic en continuar, redirigir a una nueva página
    if st.button("Continuar"):
        st.session_state.page = "pagina2"

# Página 2 con 3 botones
def show_page2():
    st.title("Página 2")
    st.write("Aquí tienes tres botones que puedes personalizar:")

    # Botones personalizables
    button_1_text = st.text_input("Texto del primer botón", "Ir a Página 3")
    button_2_text = st.text_input("Texto del segundo botón", "Ir a Página 4")
    button_3_text = st.text_input("Texto del tercer botón", "Acción Personalizada")

    if st.button(button_1_text):
        st.session_state.page = "pagina3"
    elif st.button(button_2_text):
        st.session_state.page = "pagina4"
    elif st.button(button_3_text):
        st.write("¡Has presionado el tercer botón! Puedes personalizar esta acción.")
    
    # Botón para regresar a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "inicio"

# Página 3
def show_page3():
    st.title("Página 3")
    st.write("Esta es la página 3. Puedes agregar más contenido aquí.")
    
    # Botón para regresar
    if st.button("Volver a la página 2"):
        st.session_state.page = "pagina2"

# Página 4
def show_page4():
    st.title("Página 4")
    st.write("Esta es la página 4. Puedes agregar más contenido aquí también.")
    
    # Botón para regresar
    if st.button("Volver a la página 2"):
        st.session_state.page = "pagina2"

if __name__ == "__main__":
    main()

