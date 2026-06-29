"""
LLM Response Evaluator
Loads sample responses, scores them, and saves the evaluation results.
"""

from utils import load_json, save_json
from scoring import score_response


def evaluate_dataset(input_file):
    """Evaluate all responses in a dataset."""
    responses = load_json(input_file)
    results = []

    for item in responses:
        result = {
            "prompt": item["prompt"],
            "response": item["response"],
            "score": score_response(item["response"])
        }
        results.append(result)

    return results


if __name__ == "__main__":
    input_file = "data/sample_responses.json"
    output_file = "data/evaluation_results.json"

    evaluation_results = evaluate_dataset(input_file)

    save_json(evaluation_results, output_file)

    print(f"Successfully evaluated {len(evaluation_results)} responses.")
    print(f"Results saved to: {output_file}")