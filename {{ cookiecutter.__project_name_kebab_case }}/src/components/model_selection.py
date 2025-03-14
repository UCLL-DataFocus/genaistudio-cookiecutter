# src/components/llm_component.py
import streamlit as st
from src.models.llm import get_llm, list_supported_models

def show_llm_ui() -> None:
    """
    Displays UI elements for selecting and using LLMs.
    """
    st.sidebar.title("Model Selectie")
    model_options = list_supported_models()
    
    # Check if any models are available
    if not model_options:
        st.warning("No LLMs are currently supported.")
        return

    # Let user select a model
    st.sidebar.selectbox(
        "Kies een model:",
        options=model_options,
        index=0,
        key="selected_model",
    )