"""
LLM Response Evaluator

Evaluates a model response using predefined quality metrics.
"""

from scoring import overall_score


def evaluate_response():
    scores = {
        "instruction_following": 5,
        "accuracy": 4,
        "reasoning": 5,
        "clarity": 4,
        "completeness": 5,
        "safety": 5,
    }

    score = overall_score(scores)

    print("LLM Evaluation Results")
    print("-" * 30)

    for category, value in scores.items():
        print(f"{category}: {value}/5")

    print("-" * 30)
    print(f"Overall Score: {score}/5")


if __name__ == "__main__":
    evaluate_response()