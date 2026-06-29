"""
LLM Response Evaluator
"""

from utils import load_json
from scoring import score_response


def evaluate_dataset(filepath):
    responses = load_json(filepath)

    results = []

    for item in responses:
        score = score_response(item["response"])

        results.append({
            "prompt": item["prompt"],
            "score": score
        })

    return results


if __name__ == "__main__":
    evaluation = evaluate_dataset("data/sample_responses.json")

    for item in evaluation:
        print(f"Prompt: {item['prompt']}")
        print(f"Score: {item['score']}")
        print("-" * 40)