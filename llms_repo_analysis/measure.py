import subprocess
import duckdb

def run_command_with_retries(repo, pr_number, retries=3):

    command = ["python3", "src/main.py", "generate-pr-description", "-r", repo, "-pr", str(pr_number)]
    
    for attempt in range(retries):
        print(f"Running command: {' '.join(command)} (Attempt {attempt + 1})")
        result = subprocess.run(command, text=True, capture_output=True)
        
        print("Output:", result.stdout)
        if result.returncode == 0:
            print("Success!")
        else:
            print(f"Error on attempt {attempt + 1}: {result.stderr}")

EXPECTED_MEASUREMENTS_PER_PR = 36

prs = {
    # "microsoft/autogen": [5808, 5667],
    "microsoft/autogen": [5667],
    "stanford-oval/storm": [148, 175],
    "gradio-app/gradio": [10664, 10616],
    "All-Hands-AI/OpenHands": [7064, 6585],
    "onyx-dot-app/onyx": [4198, 4112],
    "open-webui/open-webui": [11163, 11089],
    "eslint/eslint": [19417, 19272],
    "huggingface/transformers.js": [1151, 1034],
    "Kong/insomnia": [8349, 8331],
    "HumanSignal/label-studio": [7117, 7116],
    "apache/fineract": [4385, 4360],
    "elastic/elasticsearch": [124143, 124089],
    "apache/hbase": [6563, 6541],
    "NationalSecurityAgency/ghidra": [7125, 7046],
    "synthetichealth/synthea": [1290, 1178],
    "microsoft/PowerToys": [35418, 37628],
    "Azure-Samples/cognitive-services-speech-sdk": [2728, 2643],
    "lepoco/wpfui": [1039, 1202],
    "AssetRipper/AssetRipper": [1651, 1365],
    "tModLoader/tModLoader": [4492, 4342]
}

def check_pr_measurements(prs_dict):
    """
    Checks if each PR in the provided dictionary has the expected number of measurements (36).
    Outputs PRs with missing or excess measurements.
    """
    db = duckdb.connect("llm_analysis.db")

    # Dictionary to store results
    missing_measurements = {}
    excess_measurements = {}

    for repo, pr_numbers in prs_dict.items():
        for pr_number in pr_numbers:
            # Query to count the number of measurements for each PR
            query = f"""
            SELECT COUNT(*) FROM GeneratedMessages gm
            JOIN CodeDiffs cd ON gm.pr_id = cd.pr_id
            WHERE cd.repository = '{repo}' AND cd.pr_number = {pr_number};
            """
            count = db.execute(query).fetchone()[0]

            if count < EXPECTED_MEASUREMENTS_PER_PR:
                missing_measurements[(repo, pr_number)] = EXPECTED_MEASUREMENTS_PER_PR - count
            elif count > EXPECTED_MEASUREMENTS_PER_PR:
                excess_measurements[(repo, pr_number)] = count - EXPECTED_MEASUREMENTS_PER_PR

    db.close()

    # Print results
    print("\n📌 PRs with missing measurements:")
    for (repo, pr_number), missing_count in missing_measurements.items():
        print(f"- Repo: {repo}, PR Number: {pr_number}, Missing {missing_count} measurements")

    print("\n📌 PRs with excess measurements:")
    for (repo, pr_number), excess_count in excess_measurements.items():
        print(f"- Repo: {repo}, PR Number: {pr_number}, Excess {excess_count} measurements")

def delete_generated_messages_for_pr(repo_name: str, pr_number: int):
    """
    Deletes all generated messages for a given PR by first finding the associated PR ID(s).

    :param repo_name: The name of the repository containing the PR.
    :param pr_number: The number of the PR to delete generated messages for.
    """
    db = duckdb.connect("llm_analysis.db")

    # Step 1: Find all PR IDs for the given repo and PR number
    pr_ids_query = f"""
    SELECT pr_id FROM CodeDiffs 
    WHERE repository = '{repo_name}' AND pr_number = {pr_number};
    """
    pr_ids = db.execute(pr_ids_query).fetchall()

    if not pr_ids:
        print(f"⚠️ No PR found for Repository: {repo_name}, PR Number: {pr_number}")
        db.close()
        return

    # Convert result into a list of PR IDs
    pr_ids = [pr_id[0] for pr_id in pr_ids]

    # Step 2: Delete related GeneratedMessages entries for all found PR IDs
    for pr_id in pr_ids:
        # First, delete related evaluations to avoid foreign key constraints
        db.execute(f"""
            DELETE FROM Evaluations 
            WHERE message_id IN (SELECT message_id FROM GeneratedMessages WHERE pr_id = '{pr_id}');
        """)

        # Now safely delete the generated messages
        db.execute(f"DELETE FROM GeneratedMessages WHERE pr_id = '{pr_id}'")

        print(f"🗑️ Deleted all generated messages for PR ID: {pr_id} (Repo: {repo_name}, PR Number: {pr_number})")

    db.close()

# Example Usage: Delete all generated messages for a specific PR
# delete_generated_messages_for_pr("microsoft/autogen", 5667)

# check_pr_measurements(prs)
for repo, pr_list in prs.items():
    for pr in pr_list:
        run_command_with_retries(repo, pr)
