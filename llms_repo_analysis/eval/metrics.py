from deepeval.metrics import AnswerRelevancyMetric, PromptAlignmentMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase
import logging
from pydantic import BaseModel

# Define JSON schema for structured outputs
class EvaluationResponse(BaseModel):
    answer: str
    confidence: float

def evaluate_deepeval(input_text, actual_output, model, metric, context):
    logging.info("🚀 Starting DeepEval evaluation with Ollama...")

    # **Answer Relevancy Metric**
    logging.debug("📊 Initializing Answer Relevancy Metric...")
    relevancy_metric = AnswerRelevancyMetric(
        threshold=0.7,
        model=model,
        include_reason=True
    )
    relevancy_test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        retrieval_context=context
    )

    logging.debug("🔍 Measuring relevancy metric...")
    relevancy_metric.measure(relevancy_test_case)
    relevancy_score = relevancy_metric.score
    logging.info(f"✅ Relevancy Score: {relevancy_score}")
    logging.debug(f"📝 Relevancy Reason: {relevancy_metric.reason if hasattr(relevancy_metric, 'reason') else 'No reason provided'}")

    # **Prompt Alignment Metric**
    logging.debug("📊 Initializing Prompt Alignment Metric...")

    if metric == "pull_request_description":
        prompt_instructions = [
            "Write a concise and professional pull request description.",
            "Follow conventional commit message guidelines (e.g., 'fix:', 'feat:', 'chore:').",
            "Summarize key changes in bullet points.",
            "Ensure clarity and readability in the description."
        ]
    elif metric == "pull_request_code_review":
        prompt_instructions = [
            "Provide a structured code review following best practices.",
            "Use a constructive and professional tone.",
        ]
    else:
        prompt_instructions = ["Provide a structured and clear response."]

    alignment_metric = PromptAlignmentMetric(
        prompt_instructions=prompt_instructions,
        model=model,
        strict_mode=True,
        async_mode=False,  
        include_reason=True
    )
    alignment_test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output
    )

    logging.debug("🔍 Measuring alignment metric...")
    alignment_metric.measure(alignment_test_case)
    alignment_score = alignment_metric.score
    logging.info(f"✅ Alignment Score: {alignment_score}")
    logging.debug(f"📝 Alignment Reason: {alignment_metric.reason if hasattr(alignment_metric, 'reason') else 'No reason provided'}")

    # **Faithfulness Metric**
    logging.debug("📊 Initializing Faithfulness Metric...")

    faithfulness_metric = FaithfulnessMetric(
        threshold=0.7,
        model=model,
        include_reason=True
    )
    faithfulness_test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        retrieval_context=context
    )

    logging.debug("🔍 Measuring faithfulness metric...")
    faithfulness_metric.measure(faithfulness_test_case)
    faithfulness_score = faithfulness_metric.score
    logging.info(f"✅ Faithfulness Score: {faithfulness_score}")
    logging.debug(f"📝 Faithfulness Reason: {faithfulness_metric.reason if hasattr(faithfulness_metric, 'reason') else 'No reason provided'}")

    return "deepeval", relevancy_score, faithfulness_score, alignment_score