# PR-Analysis with LLM 🚀

This project provides a set of commands for analyzing and evaluating Pull Requests (PRs) using locally running LLMs. Additionally, the results can be evaluated using DeepEval and human feedback.

### 1. Clone the Repository 🔗
```bash
git clone git@git.i.mercedes-benz.com:LOBERNH/bachelor-thesis---LLMs-for-RepoAnalysis.git
```

### 2. Navigate to the Project Directory 📂
```bash
cd llms_repo_analysis
```

### 3. Create the Database 🗄️
```bash
python src/main.py create-db
```

### 4. Install Dependencies 📦
```bash
pip install -r requirements.txt
```

### 5. Set the Model for DeepEval 🧠
```bash
deepeval set-ollama deepseek-coder:6.7b
```
Or with a custom base URL:
```bash
deepeval set-ollama deepseek-coder:6.7b --base-url="http://localhost:11434/v1/"
```

### 6. Generate an Analysis with Automatic Evaluation using DeepEval Metrics 📊
Choose between generating a PR description(a) or a code review(b).

### a. Generate PR Description 📝
Generates a description for a Pull Request.
```bash
python src/main.py generate-pr-description --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```
**Options:**
- `--pullrequest, -pr` : The number of the Pull Request.
- `--repo, -r` : The repository in the format `owner/repo`.
- `--enterprise, -e` : Flag indicating if the repository is an Enterprise repository. Default: `False`.

---

### b. Add Code Review 💬
Adds code review comments to a specific Pull Request.
```bash
python src/main.py add-code-review --pullrequest <PR_NUMBER> --repo <REPO> [--enterprise]
```
**Options:**
- `--pullrequest, -pr` : The number of the Pull Request.
- `--repo, -r` : The repository in the format `owner/repo`.
- `--enterprise, -e` : Flag indicating if the repository is an Enterprise repository. Default: `False`.

### 7. Evaluation with Human Feedback 🧑‍💻
Launches a Streamlit application for manually evaluating metrics with human feedback.
```bash
python src/main.py evaluation-hf
```
---

### 8. Generate a Report *(Coming Soon)* 📈
Generates a report.
```bash
python src/main.py report
```

---

## Notes ℹ️ 
- Use `evaluation-hf` only after conducting a code review or PR description generation.
- Ensure all dependencies are installed and the database is created before running the commands.

