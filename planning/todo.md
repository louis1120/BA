# PR Reviewer Tool TODO Checklist

This checklist outlines all the tasks required to build the PR Reviewer Tool. Each section corresponds to a major module or step in the project. Mark tasks as complete as you progress.

---

## 1. Project Initialization & Setup
- [ ] Create a `requirements.txt` file including:
    - [ ] Typer
    - [ ] PyGithub
    - [ ] DuckDB or SQLite (whichever you choose)
    - [ ] Additional libraries as needed

---

## 2. CLI Foundation with Typer
- [ ] **CLI Skeleton**
  - [ ] Create a main CLI file (e.g., `main.py`) in the project root.
  - [ ] Initialize Typer and set up the basic CLI structure.
  - [ ] Implement placeholder commands:
    - [ ] `generate-pr-description` (prints "Generating PR description...")
    - [ ] `add-code-review` (prints "Adding code review comments...")
    - [ ] `report` (prints "Generating report...")
  - [ ] Wire the commands together in the Typer app.
  - [ ] Add basic docstrings and inline comments for clarity.

---

## 3. GitHub Integration Module
- [ ] **Create GitHub Integration**
  - [ ] Create a new module: `src/github_integration.py`.
  - [ ] Use PyGithub to set up the GitHub API client.
  - [ ] Read authentication tokens from environment variables:
    - [ ] For Enterprise GitHub: `GITHUB_ENTERPRISE_TOKEN` and `GH_ENTERPRISE_HOST`
    - [ ] For Public GitHub: `GH_TOKEN` and `GH_HOST`
  - [ ] Implement a function (e.g., `get_github_instance()`) to return the authenticated client.
  - [ ] Include error handling for missing or invalid tokens.


---

## 4. AI Model Integration Wrappers
- [ ] **Create AI Model Module**
  - [ ] Create a module: `src/ai_models.py`.
  - [ ] Define a base interface for AI model interactions.
  - [ ] Implement wrapper functions or classes for:
    - [ ] `qwen2.5-coder:14B`
    - [ ] `deepseek-r1:14B`
  - [ ] Simulate AI responses using dummy outputs (e.g., "Simulated response for: {prompt}").
  - [ ] Provide a mechanism to select a model or combine outputs.
  - [ ] Write unit tests to verify that the wrappers return the dummy responses.

---

## 5. PR Description Generation Module
- [ ] **Develop PR Description Module**
  - [ ] Create a module: `src/pr_description.py`.
  - [ ] Write a function `generate_pr_description(commits: List[dict]) -> str`:
    - [ ] Accept commit data with keys like `message` and `diff`.
    - [ ] Use AI model wrappers to generate a summary.
    - [ ] Structure the output to include:
      - [ ] Title
      - [ ] Summary of changes
      - [ ] Key updates
      - [ ] Additional context
  - [ ] Write unit tests using sample commit data.
  - [ ] Ensure proper error handling for AI model failures.
  - [ ] Integrate this module with the CLI command `generate-pr-description`.

---

## 6. Code Review Comments Generation Module
- [ ] **Develop Code Review Module**
  - [ ] Create a module: `src/code_review.py`.
  - [ ] Write a function `generate_code_review_comments(files: Dict[str, str]) -> List[dict]`:
    - [ ] Accept file name and file content or diff as inputs.
    - [ ] Use AI model wrappers to generate review comments.
    - [ ] Include details for each comment:
      - [ ] File name
      - [ ] Line number (simulate if necessary)
      - [ ] Comment text
      - [ ] Rationale
      - [ ] Severity (e.g., "Minor", "Critical")
  - [ ] Write unit tests with dummy file diffs.
  - [ ] Integrate this module with the CLI command `add-code-review`.

---

## 7. Interactive Feedback System
- [ ] **Implement Feedback Module**
  - [ ] Create a module: `src/feedback.py`.
  - [ ] Write a function `collect_feedback(generated_output: str) -> dict`:
    - [ ] Display the generated PR description or code review comments.
    - [ ] Prompt the user to mark output as "accurate" or "hallucinated".
    - [ ] Provide an option to retry the generation process.
    - [ ] Include input validation and error messages.
  - [ ] Write tests using input mocking to verify the feedback flow.
  - [ ] Integrate feedback functionality into the appropriate CLI commands.

---

## 8. Logging and Metrics Module
- [ ] **Develop Logging & Metrics**
  - [ ] Create a module: `src/logging_metrics.py`.
  - [ ] Connect to a local DuckDB or SQLite database for metrics persistence.
  - [ ] Implement functions to log:
    - [ ] Hallucination rates
    - [ ] Response times
    - [ ] Accuracy of suggestions
    - [ ] Number of retries
  - [ ] Ensure proper error handling for database access.
  - [ ] Write unit tests simulating metric logging.

---

## 9. Reporting Module
- [ ] **Create Reporting Module**
  - [ ] Create a module: `src/reporting.py`.
  - [ ] Write a function to generate a comprehensive PR review summary report that includes:
    - [ ] Updated PR description (title, summary, key updates, additional context)
    - [ ] Code review comments (file, line, comment, rationale, severity)
    - [ ] Performance metrics (response time, hallucination rate, accuracy)
    - [ ] Model usage statistics
    - [ ] Issues encountered during processing
    - [ ] User feedback summary
  - [ ] Format the report (e.g., as markdown).
  - [ ] Write unit tests to verify report formatting and content.
  - [ ] Integrate this module with the CLI command `report`.

---

## 10. Integration and Final Wiring
- [ ] **Integrate All Modules**
  - [ ] Update `main.py` to import:
    - [ ] GitHub integration
    - [ ] AI model wrappers
    - [ ] PR description generation
    - [ ] Code review generation
    - [ ] Feedback collection
    - [ ] Logging/metrics
    - [ ] Reporting modules
  - [ ] Ensure CLI commands (`generate-pr-description`, `add-code-review`, `feedback`, `report`) execute the full workflow:
    1. Authenticate with GitHub.
    2. Retrieve or simulate data (commits, file diffs).
    3. Call the respective generation function.
    4. Prompt for interactive feedback.
    5. Log performance and metrics.
    6. Generate and display the final report.
  - [ ] Implement robust error handling to prevent orphaned or incomplete processes.
  - [ ] Write integration tests to simulate full CLI workflows.

---

## 11. Testing Suite Development
- [ ] **Develop Comprehensive Tests**
  - [ ] Write end-to-end tests simulating the complete CLI run, including user input (using mocking).
  - [ ] Add clear instructions in the README on how to run the tests (e.g., using pytest).

---

## 12. Documentation
- [ ] **Documentation & README**
  - [ ] Update README with:
    - [ ] Project overview
    - [ ] Setup instructions
    - [ ] Usage instructions
    - [ ] Testing instructions
  - [ ] Add inline code comments and docstrings where necessary.

---

## 13. Final Review and Cleanup
- [ ] **Review & Quality Assurance**
  - [ ] Ensure there is no orphaned or dangling code.
  - [ ] Confirm that all components are fully integrated.
  - [ ] Validate robust error handling across modules.
  - [ ] Verify that all tests pass with sufficient coverage.
  - [ ] Conduct a final code review and cleanup.

---

*Use this checklist to track your progress as you develop the PR Reviewer Tool. Mark each item complete when done, and feel free to add further sub-tasks as needed.*
