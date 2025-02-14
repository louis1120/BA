# Welche Modelle kommen in die engere Auswahl?

### Kriterien
- Läuft auf gängigem Laptop (16GB RAM) > ca 14b parameter
- Unterstützt die nutzung von Tools
- eignet sich zur Codebewertung

###

| Modell                     | HumanEval | BigCodeBench | Parameter | Context |
|----------------------------|-----------|------|-----------|-----------|
| qwen2.5-Coder 7B Instruct  | 88,4%     | -    | 7B        | 128.000  |
| qwen2.5 7B Instruct        | 84,8%     |20,3  | 7B        | 131.072  |
| qwen2.5 14B Instruct       | 83,5%     | -    | 14B       | 131.072  |
| qwen2.5-Coder-14B-Instruct | -         | 26,6 | 14B       | 131.072  |
| Phi-4                      | 82,8%     | 27,4 | 14,7      | 16.000   |



Quellen für Auswahl der Modelle
[Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/)
- deepseek r1
- qwen coder
sonst gemini oder openai models
[HF- Big Code Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
Base models
Code llama zu groß mit 70b
DeepSeek-coder 33b [DeepSeek-coder 33b](https://ollama.com/library/deepseek-coder)
qwen2.5coder 32b
[BigCodeBench](https://bigcode-bench.github.io/)
unter 15b Parameter 

Eigentlich das beste bei LLM Exploer kann man nach der VRAM schauen

[llm stats](https://llm-stats.com/)
Benchmark HumanEval
1. qwen2.5-Coder 7B Instruct => 88,4% (Context 128.000)
2. qwen2.5 7B Instruct => 84,8% (Context 131.072)
3. qwen2.5 14B Instruct => 83,5% (Context 131.072)
4. Phi-4 => 82,8% (Context 16.000)
![llm-stats bis 15b parameter](image-2.png)
[LLM Explorer](https://llm.extractum.io/list/?codegen)
Code-Generation Large Language Models

[RepoBench](https://arxiv.org/abs/2306.03091) => sehr gute Benchmark für unseren Usecase
### Bewertung von einzelnen Codeblöcken

1. 50 Zeilen
2. 100 Zeilen
3. 250 Zeilen
4. 500 Zeilen

Jeweils Generiert mit dem Chat und bewertet mit pylint vor und nach den Verbesserungen
Pylint anpassen, sodass Dokumentation weniger gewichtet wird

Testcode mithilfe von ChatGPT erstellt
        import os

        data = ""

        def read_file(filename):
            global data
            f = open(filename, "r")  
            data = f.read()
            f.close()
            return data

        def process_text(text):
            words = text.split(" ")  
            result = {}
            
            for w in words:
                if w in result:
                    result[w] += 1
                else:
                    result[w] = 1
            
            return result

        def main():
            file = "sample.txt"
            
            if not os.path.exists(file):  
                print("Datei nicht gefunden!")
                return
            
            text = read_file(file)
            word_counts = process_text(text)

            # Fehlerhafte Ausgabe
            for key in word_counts.keys():
                print(key + " : " + str(word_counts[key]))  

        main()
