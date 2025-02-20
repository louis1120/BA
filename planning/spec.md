# PR Reviewer Tool Specification

This comprehensive specification should provide a clear roadmap for the LLM-based PR-reviewing tool. 

## Overview

The PR Reviewer Tool is designed to generate descriptions for new or existing pull requests (PRs) based on commit history (code diffs and messages) and create code reviews through comments, providing suggestions for code improvements. The tool will use the models qwen2.5-coder:14B and deepseek-r1:14B for these tasks. It will be implemented as a Python CLI tool using PyGithub and Typer, with potential for a TUI using Textual.

## Requirements

### Core Features

#### PR Description Generation

- Summarize changes and highlight key updates using conventional commit messages.
- Create summaries based on code diffs with commit messages as extra context.

#### Code Review Comments

- Provide high-level suggestions, specific code improvements, and potential bug identifications.
- Allow comments on specific lines using PyGithub.

#### User Interaction

- CLI tool using Typer, with potential for TUI using Textual.
- Read authentication from environment variables (GITHUB_ENTERPRISE_TOKEN and GH_ENTERPRISE_HOST for enterprise, GH_TOKEN and GH_HOST for public GitHub).
- Option to approve comments by default or use `-y` flag.
- Interactive feedback prompts at the end of each run for tagging changes as accurate or hallucination.
- Option to retry AI suggestions for hallucinated comments or descriptions.

#### Logging and Metrics

- Track hallucination rates, response time, accuracy of suggestions, and user feedback.
- Store logs and metrics locally in DuckDB or SQLite.
- Update metrics with each retry and track the number of retries.

#### Output and Reporting

- Generate a summary report with PR description updates, code review comments, performance metrics, model usage, issues encountered, and user feedback.
- Provide visual indicators and messages for the review process.

#### Additional Features

- Support for re-running reviews on updated PRs.
- Built-in help or documentation with `--help` flag.

## Architecture

### Components

#### CLI Interface

- Implemented using Typer for command-line interactions.
- Commands for generating PR descriptions, adding code review comments, and providing feedback.

#### GitHub Integration

- Use PyGithub to interact with the GitHub API.
- Authenticate using environment variables.

#### AI Models

- Integrate qwen2.5-coder:14B and deepseek-r1:14B for generating descriptions and comments.
- Allow user to select the model or use a combination.

#### Feedback System

- Interactive prompts for user feedback on generated comments and descriptions.
- Option to retry AI suggestions for hallucinated outputs.

#### Logging and Metrics

- Store logs and metrics in DuckDB or SQLite.
- Track performance metrics and hallucination rates.

#### Reporting

- Generate a summary report with detailed information on the review process.
- Provide visual indicators and messages.

## Data Handling

### Authentication

- Read from environment variables:
    - GITHUB_ENTERPRISE_TOKEN and GH_ENTERPRISE_HOST for enterprise GitHub.
    - GH_TOKEN and GH_HOST for public GitHub.

### Logging and Metrics

- Store locally in DuckDB or SQLite.
- Track:
    - Hallucination rates.
    - Response time.
    - Accuracy of suggestions.
    - User feedback.
    - Number of retries.

## Error Handling

### Strategies

#### API Errors

- Handle GitHub API errors gracefully with retry logic and informative error messages.

#### Model Errors

- Catch and log errors from AI model interactions.
- Provide fallback mechanisms or retry options.

#### User Input Errors

- Validate user inputs and provide clear error messages for invalid inputs.

#### File and Database Errors

- Handle file and database access errors with appropriate logging and recovery mechanisms.

## Testing Plan

### Manual Testing

#### Functionality Testing

- Test PR description generation with various commit histories.
- Test code review comments on different codebases (TypeScript, Java, Python).
- Test interactive feedback prompts and retry options.

#### Performance Testing

- Measure response times for generating descriptions and comments.
- Track hallucination rates and accuracy of suggestions.

#### User Experience Testing

- Evaluate the CLI interface for usability and clarity.
- Test visual indicators and messages for the review process.

#### End-to-End Tests

- Run complete workflows to ensure the tool functions as expected.

## Summary Report Format

### PR Review Summary Report

#### 📝 PR Description Update

- **Title:** Updated PR Title
- **Summary of Changes:**
    - Summarized changes here
- **Key Updates:**
    - `fix:` Fixed issue with...
    - `chore:` Updated dependencies...
- **Additional Context:**
    - Relevant commit messages here

#### 🛠️ Code Review Comments

| File       | Line | Comment                                              | Rationale                        | Severity  |
|------------|------|------------------------------------------------------|----------------------------------|-----------|
| src/main.py| 42   | Consider renaming variable `x` to `more_descriptive_name` | Improves code readability        | 🟢 Minor  |
| src/utils.js| 88  | Potential bug: Check for null before accessing property `foo` | Prevents runtime errors          | 🔴 Critical|

#### ⏱️ Performance Metrics

- **Response Time:** 2.5 seconds
- **Hallucination Rate:** 5%
- **Accuracy of Suggestions:** 95%

#### 📊 Model Usage

- **qwen2.5-coder:14B:** 60%
- **deepseek-r1:14B:** 40%


#### 📈 User Feedback

- **Rating:** 4.5/5
- **Comments:** The suggestions were very helpful!


