{%- set user_llms = cookiecutter["llm's (comma-separated, press Enter for all)"] -%}
{%- set azure_chosen = ("gpt-4o" in user_llms) or ("gpt-4o-mini" in user_llms) -%}

import os
from dotenv import load_dotenv

# === 🔧 Environment Variables & Configuration ===

# Load environment variables from the secret config file
load_dotenv("Config/.env.secret")

# === 🔧 LLM Configuration Check ===

{%- if "gpt-4o" in user_llms %}
def has_gpt_4o_config() -> bool:
    return all([
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_GPT4O_DEPLOYMENT"),
        os.getenv("AZURE_GPT4O_API_VERSION"),
    ])
{% endif %}

{%- if "gpt-4o-mini" in user_llms %}
def has_gpt_4o_mini_config() -> bool:
    return all([
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_GPT4OMINI_DEPLOYMENT"),
        os.getenv("AZURE_GPT4OMINI_API_VERSION"),
    ])
{% endif %}

{%- if "mistral-nemo" in user_llms %}
def has_mistral_config() -> bool:
    return all([
        os.getenv("MISTRAL_API_KEY"),
        os.getenv("MISTRAL_ENDPOINT"),
    ])
{% endif %}

{%- if "llama3" in user_llms %}
def has_llama3_config() -> bool:
    return all([
        os.getenv("LLAMA3_API_KEY"),
        os.getenv("LLAMA3_ENDPOINT"),
    ])
{% endif %}
# === 🌍 API Keys & Endpoints ===

{%- if azure_chosen %}
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
{% endif %}

{%- if "gpt-4o" in user_llms %}
AZURE_GPT4O_DEPLOYMENT = os.getenv("AZURE_GPT4O_DEPLOYMENT")
AZURE_GPT4O_API_VERSION = os.getenv("AZURE_GPT4O_API_VERSION")
{% endif %}

{%- if "gpt-4o-mini" in user_llms %}
AZURE_GPT4OMINI_DEPLOYMENT = os.getenv("AZURE_GPT4OMINI_DEPLOYMENT")
AZURE_GPT4OMINI_API_VERSION = os.getenv("AZURE_GPT4OMINI_API_VERSION")
{% endif %}

{%- if "mistral-nemo" in user_llms %}
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_ENDPOINT = os.getenv("MISTRAL_ENDPOINT")
{% endif %}

{%- if "llama3" in user_llms %}
LLAMA3_API_KEY = os.getenv("LLAMA3_API_KEY")
LLAMA3_ENDPOINT = os.getenv("LLAMA3_ENDPOINT")
{%- endif %}