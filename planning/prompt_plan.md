# PR Reviewer Tool Blueprint and Prompts

This document provides a comprehensive, iterative blueprint for building the PR Reviewer Tool, along with a series of step-by-step prompts. Each prompt is designed to be implemented in a test-driven manner, ensuring incremental progress and strong testing practices. The goal is to integrate all components—from the CLI interface to AI model integration and reporting—without leaving any orphaned code.

---

## Project Blueprint Overview

### 1. Project Initialization & Setup
- **Repository & Structure:**  
  - Create a Python project repository with a standard layout (e.g., `src/`, `tests/`, etc.).  
  - Use a virtual environment and include a requirements file (with `Typer`, `PyGithub`, and database libraries like DuckDB/SQLite).

### 2. CLI Foundation with Typer
- **Core CLI Structure:**  
  - Build a CLI skeleton using Typer with basic commands: `generate-pr-description`, `add-code-review`, `feedback`, and `report`.

### 3. GitHub Integration Module
- **Authentication & API Interaction:**  
  - Implement a module to connect to GitHub using PyGithub, reading tokens from environment variables (supporting both enterprise and public GitHub).  
  - Include error handling and testing.

### 4. AI Model Integration
- **Model Wrappers:**  
  - Create wrappers for the AI models (`qwen2.5-coder:14B` and `deepseek-r1:14B`) that provide a unified method for generating output.  
  - Simulate responses initially with dummy outputs.

### 5. PR Description Generation Module
- **Summarization Logic:**  
  - Build a module to generate PR descriptions from commit history (commit messages and diffs) using the AI models.  
  - Structure the output into title, summary, key updates, and additional context with appropriate tests.

### 6. Code Review Comments Generation Module
- **Review Comment Generation:**  
  - Implement a module to generate code review comments for file diffs.  
  - Each comment should include file name, line number, comment text, rationale, and severity.  
  - Include testing to verify output structure.

### 7. Interactive Feedback System
- **User Feedback & Retry:**  
  - Create an interactive system to collect user feedback on generated outputs, including options to mark outputs as “accurate” or “hallucinated” and to retry.
  
### 8. Logging and Metrics Module
- **Metrics & Persistence:**  
  - Implement logging for metrics (hallucination rates, response times, accuracy, retry counts) using DuckDB or SQLite, with proper error handling and tests.

### 9. Reporting Module
- **Summary Report Generation:**  
  - Develop a reporting module that collates all outputs and metrics into a comprehensive PR review summary report (formatted in markdown).

### 10. Integration and Wiring Together
- **Final Assembly:**  
  - Integrate all modules into the main Typer CLI application ensuring that each command triggers the correct workflow.
  
### 11. Testing Strategy
- **Test-Driven Approach:**  
  - Write unit, integration, and end-to-end tests to validate each module and the overall workflow using a test runner like pytest.

---

## Iterative Prompts for Code Generation

Each prompt is wrapped in code tags and designed to build on the previous steps.

---

### Prompt 1: Project Setup and CLI Skeleton

Prompt 1:

```
You are tasked with initializing the project structure for the PR Reviewer Tool. Create a basic Python project with the following layout:
- A `src/` directory for the source code.
- A `tests/` directory for unit and integration tests.
- A main CLI file (e.g., `main.py`) that uses Typer to define a command-line interface with placeholder commands: `generate-pr-description`, `add-code-review`, `feedback`, and `report`.

Ensure that:
- The CLI is implemented using Typer.
- Each command prints a simple confirmation message (e.g., "Generating PR description...") so that we can verify the CLI wiring.
- The project uses a requirements file listing Typer (and any other libraries you think necessary for now).

End by wiring the commands together in the Typer app. Also include basic docstrings for clarity.
```

### Prompt 2: GitHub Integration Module
```
Extend the project by implementing a GitHub integration module. Create a new module (e.g., `github_integration.py`) in the `src/` directory. This module should:
- Use PyGithub to connect to the GitHub API.
- Read authentication tokens from environment variables. Support two scenarios:
  - Enterprise GitHub using `GITHUB_ENTERPRISE_TOKEN` and `GH_ENTERPRISE_HOST`
  - Public GitHub using `GH_TOKEN` and `GH_HOST`
- Provide a function (e.g., `get_github_instance()`) that returns an authenticated GitHub client.
- Include error handling for missing or invalid tokens.
- Write a test case that simulates reading environment variables and creating a GitHub client (mocking PyGithub if needed).

Ensure that the module is self-contained and can be imported and used by other parts of the application.
```


### Prompt 3: AI Model Integration Wrappers
```
Develop a module named `ai_models.py` that abstracts interactions with the two AI models: `qwen2.5-coder:14B` and `deepseek-r1:14B`. This module should:
- Define a base interface for model interactions.
- Create wrapper classes or functions for each model that provide a unified method (e.g., `generate_output(prompt: str) -> str`).
- For now, simulate the AI responses with dummy outputs (e.g., return "Simulated response for: " + prompt).
- Allow for selecting a model (or combination) based on input parameters.
- Include unit tests that validate the behavior of these wrappers (ensure they return the dummy response).

Focus on clean, testable code, and ensure this module is independent of the CLI logic.
```

### Prompt 4: PR Description Generation Module
Implement a new module called `pr_description.py` that generates a PR description from commit history data. This module should:
- Define a function (e.g., `generate_pr_description(commits: List[dict]) -> str`) that accepts a list of commit data. Each commit dict may contain keys like `message` and `diff`.
- Use the AI model wrappers from `ai_models.py` to generate a summary based on the commit messages and diffs.
- Structure the output to include a title, summary of changes, key updates, and additional context.
- Write unit tests that provide sample commit data and verify that the output contains the expected sections.
- Ensure that errors in AI model responses are handled gracefully.

At the end, wire this module so that the CLI command `generate-pr-description` calls this function.


### Prompt 5: Code Review Comments Generation Module
```
Create a new module called `code_review.py` to handle the generation of code review comments. This module should:
- Provide a function (e.g., `generate_code_review_comments(files: Dict[str, str]) -> List[dict]`) where the key is a file name and the value is the file content or diff.
- Use the AI model wrappers to generate review comments for each file. Each comment should include:
  - The file name and line number (simulate with a fixed line number if needed)
  - A comment text with a rationale and severity (e.g., "Minor", "Critical")
- Write unit tests that supply dummy file diffs and validate that comments are generated with the proper structure.
- Ensure the function is robust and integrates with the GitHub integration module for future commenting capabilities.

Wire this module to the CLI command `add-code-review` so that when triggered, it calls the function and prints the simulated review comments.
```

### Prompt 6: Interactive Feedback System
```
Implement an interactive feedback module named `feedback.py`. This module should:
- Provide a function (e.g., `collect_feedback(generated_output: str) -> dict`) that displays the generated PR description or review comments and prompts the user for feedback.
- Allow the user to mark the output as "accurate" or "hallucinated" and optionally trigger a retry of the generation process.
- Integrate input validation and clear error messages for invalid entries.
- Write tests (using input mocking) to ensure that the feedback flow works as expected.

Integrate this feedback function with the respective CLI commands so that after generating a description or review comments, the tool prompts the user for feedback.
```

Prompt 7: Logging and Metrics Module
```
Develop a module named `logging_metrics.py` that handles logging and performance metrics. This module should:
- Connect to a local DuckDB or SQLite database to persist metrics.
- Provide functions to log the following:
  - Hallucination rates
  - Response times
  - Accuracy of suggestions
  - Number of retries
- Ensure that database errors are caught and logged appropriately.
- Write unit tests that simulate logging and verify that metrics are recorded in the database.

Finally, ensure that all major functions (PR description generation, code review comments, feedback) call the appropriate logging functions.
```


#### Prompt 8: Reporting Module
```
Implement a reporting module called `reporting.py` that generates a comprehensive PR review summary report. This report should include:
- Updated PR Description (with title, summary, key updates, additional context)
- Code review comments (with file, line, comment, rationale, severity)
- Performance metrics (response time, hallucination rate, accuracy)
- Model usage statistics
- Issues encountered during processing
- User feedback summary

The report should be formatted clearly (for example, as a markdown document). Write unit tests that validate the report format and content given sample inputs.

Wire this reporting function to the CLI command `report` so that invoking it outputs the full summary.
```

### Prompt 9: Integration and Final Wiring in the CLI
```
Integrate all the previously developed modules into the main CLI application. Update your `main.py` (or equivalent) to:
- Import and wire together the GitHub integration, AI model wrappers, PR description generation, code review generation, feedback collection, logging/metrics, and reporting modules.
- Ensure each CLI command (`generate-pr-description`, `add-code-review`, `feedback`, `report`) executes the full workflow:
  1. Authenticate with GitHub.
  2. Retrieve or simulate necessary data (commits, file diffs).
  3. Call the respective generation function (PR description or code review).
  4. Prompt the user for interactive feedback.
  5. Log the performance and metrics.
  6. Generate and display the final report.
- Make sure that error handling is in place so that if one step fails, it does not leave orphaned code or incomplete state.
- Write an integration test (or describe one) that simulates a complete run through the CLI commands.

Document the overall flow in the code comments for clarity.

```