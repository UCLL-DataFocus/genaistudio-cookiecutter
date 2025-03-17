from typing import cast
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import ChatCompletions
from azure.core.credentials import AzureKeyCredential

class Llama3LLM:
    def __init__(self, api_key: str, endpoint: str) -> None:
        self.api_key = api_key
        self.endpoint = endpoint
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint, 
            credential=AzureKeyCredential(self.api_key)
        )

    def invoke(self, prompt: str) -> object:
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2048,
            "temperature": 0.8,
            "top_p": 0.1,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }

        try:
            response = self.client.complete(payload)
            completions = cast(ChatCompletions, response)
            return type("Response", (), {"content": completions.choices[0].message.content})()
        except Exception as e:
            return type("Response", (), {"content": f"Error: {str(e)}"})()
