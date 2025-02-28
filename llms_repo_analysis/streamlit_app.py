from src.logging_metrics import insert_evaluation
import streamlit as st
import random
import duckdb

def get_unevaluated_message_ids():
    db = duckdb.connect("llm_analysis.db")
    result = db.execute("""
        SELECT message_id 
        FROM GeneratedMessages 
        WHERE message_id NOT IN (
            SELECT message_id FROM Evaluations WHERE evaluation_method = 'humanfeedback'
        )
    """).fetchall()
    return [row[0] for row in result]

def fetch_message_data(message_id):
    db = duckdb.connect("llm_analysis.db")
    result = db.execute("""
        SELECT g.generated_output, g.prompt_id, c.diff_text, c.commit_messages 
        FROM GeneratedMessages g 
        LEFT JOIN CodeDiffs c ON g.pr_id = c.pr_id
        WHERE g.message_id = ?
    """, (message_id,)).fetchone()
    if not result:
        return None, None, None, None
    generated_output, prompt_id, diff_text, commit_messages = result
    prompt_result = db.execute("SELECT prompt_text FROM Prompts WHERE prompt_id = ?", (prompt_id,)).fetchone()
    if not prompt_result:
        raise ValueError("Prompt ID not found in the database")
    prompt_template = prompt_result[0]
    return generated_output, prompt_template, diff_text, commit_messages

def human_feedback_evaluation():
    st.set_page_config(layout="wide")
    st.title("Human Feedback Evaluation")
    unevaluated_message_ids = get_unevaluated_message_ids()
    if not unevaluated_message_ids:
        st.write("No unevaluated messages found.")
        return
    selected_message_id = random.choice(unevaluated_message_ids)
    generated_output, prompt, diff_text, commit_messages = fetch_message_data(selected_message_id)
    if not generated_output:
        st.write("Failed to retrieve message data.")
        return
    col1, spacer, col2 = st.columns([4, 0.2, 1.5])
    with col1:
        st.markdown("### Prompt:")
        st.text_area("", prompt, height=150, disabled=True)

        st.markdown("### Context:")
        if diff_text:
            st.markdown("#### Code Diff:")
            st.code(diff_text, language='diff')
        if commit_messages:
            st.markdown("#### Commit Messages:")
            st.text_area("", commit_messages, height=80, disabled=True)

        st.markdown("### Generated Output:")
        st.text_area("", generated_output, height=200, disabled=True)
    
    with col2:    
        if "alignment_score" not in st.session_state:
            st.session_state.alignment_score = 5
        if "relevancy_score" not in st.session_state:
            st.session_state.relevancy_score = 5
        if "faithfulness_score" not in st.session_state:
            st.session_state.faithfulness_score = 5

        st.markdown("#### Alignment")
        st.write("Rate how well the generated output aligns with the prompt.")
        alignment_score = st.slider("", 0, 10, st.session_state.alignment_score, key="alignment_slider") / 10

        st.markdown("#### Relevance")
        st.write("Rate how relevant the generated output is in the context of the prompt.")
        relevancy_score = st.slider("", 0, 10, st.session_state.relevancy_score, key="relevancy_slider") / 10

        st.markdown("#### Faithfulness")
        st.write("Rate how accurately the generated output reflects the context.")
        faithfulness_score = st.slider("", 0, 10, st.session_state.faithfulness_score, key="faithfulness_slider") / 10

        evaluation_method = "humanfeedback"
        evaluation_model = None
        
        if st.button("Next"):
            insert_evaluation(selected_message_id, evaluation_method, evaluation_model, relevancy_score, faithfulness_score, alignment_score)
            st.session_state.alignment_score = 5
            st.session_state.relevancy_score = 5
            st.session_state.faithfulness_score = 5
            st.session_state["reload"] = True
            st.rerun()

if __name__ == "__main__":
    human_feedback_evaluation()