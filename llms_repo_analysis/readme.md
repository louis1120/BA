# PR Analysis with LLM 🚀

This project provides a set of commands for analyzing and evaluating pull requests (PRs) using locally running LLMs. Additionally, the results can be evaluated with DeepEval and human feedback.

## Setup

### 1. Clone the repository 🔗
```bash
git clone git@git.i.mercedes-benz.com:LOBERNH/bachelor-thesis---LLMs-for-RepoAnalysis.git
```

### 2. Navigate to the project directory 📂
```bash
cd llms_repo_analysis
```

### 3. Install Ollama 🦙
[Ollama Download](https://ollama.com/download/)

If Ollama is not installed yet, it can be set up using the following command:

#### Linux/macOS:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows:
1. Install WSL2.
2. Start Ubuntu in WSL and run the following command:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

---

### 4. Start the Ollama server 🦙
```bash
ollama serve
```
This command starts the Ollama server, which is required for local LLM usage.

---

### 5. Measure with all registered Models 📂
If your own **model files** are located in the `modelfiles` folder, they can be registered with Ollama:

```bash
cd modelfiles
ollama create deepseek_temp02 -f deepseek_temp02.Modelfile
ollama create deepseek_temp07 -f deepseek_temp07.Modelfile
ollama create qwen_temp02 -f qwen_temp02.Modelfile
ollama create qwen_temp07 -f qwen_temp07.Modelfile
```

---

### 6. Alternatively: Use a custom model in the code
For measurement purposes, all models registered in `ai_models.py` are used. If only a specific model should be used, the code needs to be adjusted.

**Important:** Models must be decorated with `@register_model`.

**Example:**
```python
@register_model
class QwenT07(AIModelBase):
    def __init__(self):
        super().__init__("qwen_t07:latest")
```

---

### 7. Create the database 🟤
```bash
python src/main.py create-db
```

### 8. Install dependencies 📦
```bash
pip install -r requirements.txt
```

---

## Generate PR descriptions and conduct code reviews with Ollama

### 1. Generate a PR description 📝
Creates a description for a pull request.

```bash
python src/main.py generate-pr-description --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```

**Options:**
- `--pullrequest, -pr` *(Required)*: The pull request number.
- `--repo, -r` *(Required)*: The repository in the format `owner/repo`.
- `--enterprise, -e` *(Optional)*: Flag indicating whether the repository is an Enterprise repository. Default: `False`.

---

### 2. Interactive PR Analysis 🛠️
Perform an interactive analysis on a pull request with a selected prompt and model.

```bash
python src/main.py interactive-perform-analysis --pullrequest <PR_NUMBER> --repo <REPO> --model <MODEL_NAME> --prompt <PROMPT>
```

**Options:**
- `--pullrequest, -pr` *(Required)*: The pull request number.
- `--repo, -r` *(Required)*: The repository in the format `owner/repo`.
- `--enterprise, -e` *(Optional)*: Flag indicating whether the repository is an Enterprise repository. Default is `False`.

---

### 3. Add a code review *(Coming Soon / Maintenance)* 💬
Adds code review comments to a specific pull request.

```bash
python src/main.py add-code-review --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```

**Options:**
- `--pullrequest, -pr` *(Required)*: The pull request number.
- `--repo, -r` *(Required)*: The repository in the format `owner/repo`.
- `--enterprise, -e` *(Optional)*: Flag indicating whether the repository is an Enterprise repository. Default: `False`.

---

✅ **Your model is now ready to use! Good luck!** 🚀
