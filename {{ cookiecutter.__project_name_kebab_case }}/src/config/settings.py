import os
from dotenv import load_dotenv

# === 🔧 Environment Variables & Configuration ===

# Load environment variables from the secret config file
load_dotenv("Config/.env.secret")

def validate_env() -> None:
    """
    Validate that all required environment variables are set.
    Raises an error if any are missing.
    """
    required = [
        "AZURE_OPENAI_API",
        "AZURE_ENDPOINT",
        "AZURE_OPENAI_DEPLOYMENT",
        "AZURE_API_VERSION",
    ]
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")

# Validate environment variables
validate_env()

# === 🌍 API Keys & Endpoints ===

AZURE_OPENAI_API = os.getenv("AZURE_OPENAI_API")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

MISTRAL_API_KEY= os.getenv("MISTRAL_API_KEY")
MISTRAL_ENDPOINT= os.getenv("MISTRAL_ENDPOINT")
