import streamlit as st

def app():
    sidebar_logo = "Images/genai-studio-logo.png"

    st.logo(sidebar_logo, icon_image=sidebar_logo, size="large")
    st.set_page_config(
        page_title="Tabblad titel",
        page_icon="Images/genai-studio-favicon.ico",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={"About": "Deze app werd gemaakt door GenAI Studio."},
    )

    st.title("{{ cookiecutter.app_name }}")
    st.write(
        """
    {{ cookiecutter.app_description }}
    """
    )

    st.sidebar.markdown(
        """
    ### Hoe het werkt
    
    Extra info in markdown.
    """
    )
  
if __name__ == "__main__":
    app()

