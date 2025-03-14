from typing import Any, Dict, List
from langchain_openai import AzureChatOpenAI
from langchain_mistralai.chat_models import ChatMistralAI
from src.config.settings import (
    AZURE_OPENAI_API,
    AZURE_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_API_VERSION,
    MISTRAL_API_KEY,
    MISTRAL_ENDPOINT,
)

# === 🤖 LLM Model Manager ===
# This module manages and caches instances of different LLMs for efficient reuse.

SUPPORTED_MODELS = [
    "gpt-4o-mini",
    "mistral-nemo",
]

# Cache to store LLM instances and avoid redundant instantiations
_llm_cache: Dict[str, Any] = {}

def get_llm(model_name: str) -> Any:
    """
    Retrieves an LLM instance from the cache if available;
    otherwise, creates one and stores it for future reuse.

    Supported models:
    - "gpt-4o-mini": Azure OpenAI GPT-4o-mini model

    Args:
        model_name (str): The name of the model to retrieve.

    Returns:
        Any: The initialized LLM instance.
    """
    if model_name in _llm_cache:
        return _llm_cache[model_name]

    # === Azure OpenAI GPT-4o-mini ===
    if model_name == "gpt-4o-mini":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            api_key=AZURE_OPENAI_API,   # type: ignore
            azure_deployment=AZURE_OPENAI_DEPLOYMENT,
            api_version=AZURE_API_VERSION,
        )
    elif model_name == "mistral-nemo":
        llm = ChatMistralAI(
            api_key=MISTRAL_API_KEY,
            base_url=MISTRAL_ENDPOINT,
        )
        
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    # Store the LLM instance in cache
    _llm_cache[model_name] = llm
    return llm

def list_supported_models() -> List[str]:
    return SUPPORTED_MODELS
