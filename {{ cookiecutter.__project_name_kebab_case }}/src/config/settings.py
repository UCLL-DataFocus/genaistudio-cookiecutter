import os
from dotenv import load_dotenv

# === 🔧 Environment Variables & Configuration ===

# Load environment variables from the secret config file
load_dotenv("Config/.env.secret")

# === 🔧 LLM Configuration Check ===
def has_openai_config() -> bool:
    return all([
        os.getenv("AZURE_OPENAI_API"),
        os.getenv("AZURE_ENDPOINT"),
        os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        os.getenv("AZURE_API_VERSION"),
    ])

def has_mistral_config() -> bool:
    return all([
        os.getenv("MISTRAL_API_KEY"),
        os.getenv("MISTRAL_ENDPOINT"),
    ])

# === 🌍 API Keys & Endpoints ===

AZURE_OPENAI_API = os.getenv("AZURE_OPENAI_API")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

MISTRAL_API_KEY= os.getenv("MISTRAL_API_KEY")
MISTRAL_ENDPOINT= os.getenv("MISTRAL_ENDPOINT")
