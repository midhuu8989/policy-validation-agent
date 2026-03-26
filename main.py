from retrieval.retriever import load_policies, search_policies
from extractor.clause_extractor import extract_clauses
from validator.validator import validate_policies
from report.report_generator import generate_report
from explainer import generate_explanation

def run_agent():

    print("\n=== POLICY VALIDATION AGENT ===\n")

    # Load data
    data = load_policies("data/policies.csv")

    # Take user input
    query = input("Enter policy query (e.g., attendance, grading, AI): ").strip().lower()

    if not query:
        print("❌ Please enter a valid query.")
        return

    # Retrieve policies
    results = search_policies(data, query)

    if results.empty:
        print("❌ No policies found for this query.")
        return

    print("\n🔍 Retrieved Policies:\n")
    for p in results["policy_text"]:
        print("-", p)

    # Extract clauses
    extracted = extract_clauses(results)

    # Validate
    validation = validate_policies(extracted)

    # Generate explanations
    explanations = generate_explanation(validation)
    
    print("\n🤖 AI ANALYSIS:\n")

    for e in explanations:
        print(f"Policy: {e['policy']}")
        print(f"Status: {e['status']}")
        print(f"Explanation: {e['explanation']}\n")

    # Final report
    report = generate_report(validation)

    print(report)


if __name__ == "__main__":
    run_agent()
