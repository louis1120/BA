# PR-Analysis with LLM 🚀

Dieses Projekt stellt eine Reihe von Befehlen zur Analyse und Bewertung von Pull Requests (PRs) mit lokal laufenden LLMs bereit. Zudem können die Ergebnisse mit DeepEval und menschlichem Feedback evaluiert werden.

## Setup

### 1. Repository klonen 🔗
```bash
git clone git@git.i.mercedes-benz.com:LOBERNH/bachelor-thesis---LLMs-for-RepoAnalysis.git
```

### 2. In das Projektverzeichnis wechseln 📂
```bash
cd llms_repo_analysis
```

### 3. Ollama installieren 🦙
[Ollama Download](https://ollama.com/download/)

### 4. Ollama-Modelle herunterladen 🦙
```bash
ollama pull deepseek-coder:6.7b
```

### 5. Ollama-Server starten 🦙
```bash
ollama serve
```

### 6. Datenbank erstellen 🗄️
```bash
python src/main.py create-db
```

### 7. Abhängigkeiten installieren 📦
```bash
pip install -r requirements.txt
```

## PR-Beschreibung generieren und Code-Review mit Ollama durchführen

### 1. PR-Beschreibung generieren 📝
Erzeugt eine Beschreibung für einen Pull Request.
```bash
python src/main.py generate-pr-description --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```
**Optionen:**
- `--pullrequest, -pr` : Die Nummer des Pull Requests.
- `--repo, -r` : Das Repository im Format `owner/repo`.
- `--enterprise, -e` : Flag, das angibt, ob das Repository ein Enterprise-Repository ist. Standard: `False`.

---

### 2. Code-Review hinzufügen 💬
Fügt Code-Review-Kommentare zu einem spezifischen Pull Request hinzu.
```bash
python src/main.py add-code-review --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```
**Optionen:**
- `--pullrequest, -pr` : Die Nummer des Pull Requests.
- `--repo, -r` : Das Repository im Format `owner/repo`.
- `--enterprise, -e` : Flag, das angibt, ob das Repository ein Enterprise-Repository ist. Standard: `False`.

---

## Generierte Ergebnisse evaluieren

### 1. Modell für DeepEval setzen 🧠
```bash
deepeval set-ollama deepseek-coder:6.7b
```
Oder mit einer benutzerdefinierten Basis-URL:
```bash
deepeval set-ollama deepseek-coder:6.7b --base-url="http://localhost:11434/v1/"
```

### 2. Evaluation mit menschlichem Feedback 🧑‍💻
Startet eine Streamlit-Anwendung zur manuellen Bewertung mit menschlichem Feedback.
```bash
python eval/evaluate.py humanfeedback
```

### 3. Evaluation mit DeepEval 📊
```bash
python eval/evaluate.py deepeval
```

### 4. Bericht generieren *(Coming Soon)* 📈
Erzeugt einen Bericht.
```bash
python eval/evaluate.py report
```
