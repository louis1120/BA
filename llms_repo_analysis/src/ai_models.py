import time
import logging
from ollama import Client, ResponseError

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

REGISTERED_MODELS = []

def register_model(cls):
    """Decorator function to register AI models by adding their model_name to a global list."""
    instance = cls()
    REGISTERED_MODELS.append(instance.model_name)
    return cls

class AIModelBase:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_response(self, prompt: str, context: str, host: str = "http://127.0.0.1:11434") -> tuple:
        try:
            client = Client(host=host)
            response = client.chat(
                model=self.model_name,
                messages=[
                    {'role': 'system', 'content': f"Here is the diff for context:\n{context}"},
                    {'role': 'user', 'content': prompt}
                ]
            )

            message_content = response.get("message", {}).get("content", "")
            total_duration = response.get('total_duration', 0) / 1e9
            load_duration = response.get('load_duration', 0) / 1e9
            prompt_tokens = response.get('prompt_eval_count', 0)
            prompt_eval_time = response.get('prompt_eval_duration', 0) / 1e9
            generated_tokens = response.get('eval_count', 0)
            generation_time = response.get('eval_duration', 0) / 1e9

            # Log the values
            logging.info(f"Model: {self.model_name}")
            logging.info(f"Message Content: {message_content}")
            logging.info(f"Total Duration: {total_duration} seconds")
            logging.info(f"Load Duration: {load_duration} seconds")
            logging.info(f"Prompt Tokens: {prompt_tokens}")
            logging.info(f"Prompt Eval Time: {prompt_eval_time} seconds")
            logging.info(f"Generated Tokens: {generated_tokens}")
            logging.info(f"Generation Time: {generation_time} seconds")

            return message_content, total_duration, load_duration, prompt_tokens, prompt_eval_time, generated_tokens, generation_time
        except ResponseError as e:
            logging.error(f"ResponseError: {e}")
            return f"ResponseError: {e}", 0.0, 0.0, 0, 0.0, 0, 0.0
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}", 0.0, 0.0, 0, 0.0, 0, 0.0

@register_model
class QwenT07(AIModelBase):
    def __init__(self):
        super().__init__("qwen_t07:latest")

@register_model
class QwenT02(AIModelBase):
    def __init__(self):
        super().__init__("qwen_t02:latest")

@register_model
class DeepseekR1T07(AIModelBase):
    def __init__(self):
        super().__init__("dsr1_t07:latest")

@register_model
class DeepseekR1T02(AIModelBase):
    def __init__(self):
        super().__init__("dsr1_t02:latest")
        
def get_ai_model(model_name: str) -> AIModelBase:
    model_classes = {
        "qwen_t07:latest": QwenT07,
        "qwen_t02:latest": QwenT02,
        "dsr1_t07:latest": DeepseekR1T07,
        "dsr1_t02:latest": DeepseekR1T02,
    }
    
    if model_name in model_classes:
        return model_classes[model_name]()
    else:
        raise ValueError(f"Unknown model name: {model_name}")
