from typing import Any, Dict, List
{% if "gpt-4o-mini" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
from langchain_openai import AzureChatOpenAI
{% endif %}
{% if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
from langchain_mistralai.chat_models import ChatMistralAI
{% endif %}
from src.config.settings import (
    {% if "gpt-4o-mini" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    AZURE_OPENAI_API,
    AZURE_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_API_VERSION,
    has_openai_config,
    {% endif %}
    {% if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    MISTRAL_API_KEY,
    MISTRAL_ENDPOINT,
    has_mistral_config,
    {% endif %}
)

# === 🤖 LLM Model Manager ===
# This module manages and caches instances of different LLMs for efficient reuse.

_AVAILABLE_MODELS = []
{% if "gpt-4o-mini" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
if has_openai_config():
    _AVAILABLE_MODELS.append("gpt-4o-mini")
{% endif %}
{% if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
if has_mistral_config():
    _AVAILABLE_MODELS.append("mistral-nemo")
{% endif %}

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

    {% if "gpt-4o-mini" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    if model_name == "gpt-4o-mini":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            api_key=AZURE_OPENAI_API,   # type: ignore
            azure_deployment=AZURE_OPENAI_DEPLOYMENT,
            api_version=AZURE_API_VERSION,
        )
    {% endif %}
    {% if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    if model_name == "mistral-nemo":
        llm = ChatMistralAI(
            api_key=MISTRAL_API_KEY,
            base_url=MISTRAL_ENDPOINT,
        )
    {% endif %}

    # Store the LLM instance in cache
    _llm_cache[model_name] = llm
    return llm

def list_supported_models() -> List[str]:
    return _AVAILABLE_MODELS
