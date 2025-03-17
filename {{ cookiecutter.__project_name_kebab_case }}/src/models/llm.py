from typing import Any, Dict, List

{% set user_llms = cookiecutter["llm's (comma-separated, press Enter for all)"] -%}
{%- set uses_gpt4o = "gpt-4o" in user_llms -%}
{%- set uses_gpt4o_mini = "gpt-4o-mini" in user_llms -%}
{% if uses_gpt4o or uses_gpt4o_mini %}from langchain_openai import AzureChatOpenAI {% endif %}
{% if "llama3" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}from src.models.custom.llama3 import Llama3LLM {% endif %}
{% if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}from langchain_mistralai.chat_models import ChatMistralAI {% endif %}
from src.config.settings import (
    {%- if uses_gpt4o %}
    AZURE_GPT4O_DEPLOYMENT,
    AZURE_GPT4O_API_VERSION,
    has_gpt_4o_config,
    {%- endif %}
    {%- if uses_gpt4o_mini %}
    AZURE_GPT4OMINI_DEPLOYMENT,
    AZURE_GPT4OMINI_API_VERSION,
    has_gpt_4o_mini_config,
    {%- endif %}
    {%- if uses_gpt4o or uses_gpt4o_mini %}
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    {%- endif %}
    {%- if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    MISTRAL_API_KEY,
    MISTRAL_ENDPOINT,
    has_mistral_config,
    {%- endif %}
    {%- if "llama3" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    LLAMA3_API_KEY,
    LLAMA3_ENDPOINT,
    has_llama3_config,
    {%- endif %}
)

# === 🤖 LLM Model Manager ===
# This module manages and caches instances of different LLMs for efficient reuse.
_AVAILABLE_MODELS = []
{% if uses_gpt4o %}
if has_gpt_4o_config():
    _AVAILABLE_MODELS.append("gpt-4o")
{% endif %}
{%- if uses_gpt4o_mini %}
if has_gpt_4o_mini_config():
    _AVAILABLE_MODELS.append("gpt-4o-mini")
{% endif %}
{%- if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
if has_mistral_config():
    _AVAILABLE_MODELS.append("mistral-nemo")
{% endif %}
{%- if "llama3" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
if has_llama3_config():
    _AVAILABLE_MODELS.append("llama3")
{%- endif %}

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

    {% if uses_gpt4o -%}
    if model_name == "gpt-4o":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,   # type: ignore
            azure_deployment=AZURE_GPT4O_DEPLOYMENT,
            api_version=AZURE_GPT4O_API_VERSION,
        )
    {% endif %}
    {%- if uses_gpt4o_mini %}
    if model_name == "gpt-4o-mini":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,   # type: ignore
            azure_deployment=AZURE_GPT4OMINI_DEPLOYMENT,
            api_version=AZURE_GPT4OMINI_API_VERSION,
        )
    {% endif %}
    {%- if "mistral-nemo" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    if model_name == "mistral-nemo":
        llm = ChatMistralAI(
            api_key=MISTRAL_API_KEY,
            base_url=MISTRAL_ENDPOINT,
        )
    {% endif %}
    {%- if "llama3" in cookiecutter["llm's (comma-separated, press Enter for all)"] %}
    if model_name == "llama3":
        llm = Llama3LLM(
            api_key=LLAMA3_API_KEY,
            endpoint=LLAMA3_ENDPOINT,
        )
    {%- endif %}

    # Store the LLM instance in cache
    _llm_cache[model_name] = llm
    return llm

def list_supported_models() -> List[str]:
    return _AVAILABLE_MODELS
