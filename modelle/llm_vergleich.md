# Welche Modelle kommen in die engere Auswahl?

Im Rahmen der Forschung wurde sich auf die Modelle qwen2.5-coder:14b (https://ollama.com/library/qwen2.5-coder:14b) und deepseek-r1:14b (https://ollama.com/library/deepseek-r1:14b) von der Platform Ollama beschränkt. Entscheidend für die Modellauswahl, war dass das LLM lokal laufen kann und dabei weniger als 16 GB Arbeitsspeicher nutzt. 
Weiterhin war wichtig, dass das Modell möglichst gut in dem Aufgabenbereich, der Programmcode entwicklung und analyse ist, wodurch sich auf Benchmarks wie HumanEval und BigCodeBench bezogen wurde.
- Was sind Benchmarks?
- Welche Benchmarks wurden warum berücksichtigt?
Zusätzlich sind nur Modelle berücksichtigt worden, welche auf Ollama zur verfügung stehen.
- Was spricht für Ollama?
Ein weiterer grund für die Modell auswahl sind die unterschiedlichen Ansätze der beiden Modelle, da deepseek-r1:14b grundsätzlich anders aufgebaut ist als qwen2.5-coder:14b.
Das Modell deepseek-r1:14b nutzt das Konzept der sog. Chain of thought.
- Was unterscheidet die chain of thaught von der "normalen" Architektur? + im Bezug auf code



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


