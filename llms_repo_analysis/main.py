from ollama import Client

def ask_local_model_stream(prompt: str, model_name: str, host: str = "http://127.0.0.1:11434"):
    """
    Sends a prompt to a local Ollama model on a custom host/port
    (model_name) and streams the response in chunks.

    :param prompt: Text/Question for the model
    :param model_name: Name/path of your local model
    :param host: Base URL where Ollama is running (includes port)
    """
    # Erstelle einen Client mit dem gewünschten Host/Port
    client = Client(host=host)

    # Starte einen Streaming-Chat
    stream = client.chat(
        model=model_name,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )

    # Chunkweise Ausgabe
    for chunk in stream:
        print(chunk["message"]["content"], end='', flush=True)

if __name__ == "__main__":
    print("Streaming response:\n")
    ask_local_model_stream("Explain the principle of the Fibonacci sequence in Python.", "deepseek-r1:14b")
    print("\n--- End of response ---")