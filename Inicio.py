import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Función para mostrar diferentes páginas según la opción seleccionada
def main():
    # Selección de página
    page = st.selectbox("Selecciona una página", ["Inicio", "Login", "Otro"])

    if page == "Inicio":
        show_home_page()
    elif page == "Login":
        show_login_page()
    elif page == "Otro":
        show_other_page()

# Página de inicio
def show_home_page():
    st.title("Página de Inicio")
    st.write("Bienvenido a la página principal.")
    st.button("Ir a Login", on_click=redirect_to_login)

# Página de Login
def show_login_page():
    st.title("Página de Login")
    st.write("Esta es la página de login.")

# Otra página
def show_other_page():
    st.title("Otra Página")
    st.write("Esto es algo más.")

# Redirección a la página de login
def redirect_to_login():
    st.session_state.page = "Login"

if __name__ == "__main__":
    main()
