import json
import requests
import asyncio
from pydantic import BaseModel, ValidationError
from jsonschema import validate, ValidationError as JSONSchemaError
from deepeval.models import DeepEvalBaseLLM
import logging

logging.basicConfig(level=logging.DEBUG)
class OllamaDeepEval(DeepEvalBaseLLM):
    def __init__(self, model_name: str, base_url: str = "http://127.0.0.1:11434"):
        """
        Initializes an Ollama-based model instance.

        :param model_name: The name of the Ollama model.
        :param base_url: The base URL of the Ollama server.
        """
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")

    def get_model_name(self):
        """Returns the model name."""
        return self.model_name

    def load_model(self):
        """Required by DeepEvalBaseLLM, but not needed for Ollama (returns None)."""
        return None 
    
    def query_ollama(self, prompt: str) -> str:
        """
        Queries the Ollama API for text generation.

        :param prompt: The input text prompt.
        :return: The raw response string from Ollama.
        """
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False  
        }

        try:
            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status() 

            return response.json().get("response", "").strip()

        except requests.RequestException as e:
            raise ConnectionError(f"❌ Error fetching response from Ollama: {str(e)}")

    def generate(self, prompt: str, schema: BaseModel) -> BaseModel:
        """
        Generates a response using Ollama and enforces valid JSON outputs.

        :param prompt: The input text prompt.
        :param schema: The expected JSON schema (Pydantic).
        :return: A structured JSON object based on the provided schema.
        """
        output = self.query_ollama(prompt)

        try:
            json_result = json.loads(output)  # Convert string to JSON
            validate(instance=json_result, schema=schema.model_json_schema())  # Validate JSON format

            return schema(**json_result)  # Return structured response

        except json.JSONDecodeError:
            raise ValueError(f"❌ Invalid JSON response from Ollama:\n{output}")

        except JSONSchemaError as e:
            raise ValueError(f"❌ JSON schema validation failed: {str(e)}")

        except ValidationError as e:
            raise ValueError(f"❌ Pydantic schema validation failed: {str(e)}")

    async def a_generate(self, prompt: str, schema: BaseModel) -> BaseModel:
        """
        Asynchronous version of `generate`, enforcing JSON outputs.

        :param prompt: The input text prompt.
        :param schema: The expected JSON schema.
        :return: A structured JSON object based on the provided schema.
        """
        return await asyncio.to_thread(self.generate, prompt, schema)
