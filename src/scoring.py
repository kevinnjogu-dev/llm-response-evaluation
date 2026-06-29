"""
LLM Response Scoring Module

Provides functions for scoring LLM responses across
multiple evaluation dimensions.
"""

from typing import Dict


def score_instruction_following(score: int) -> int:
    return max(1, min(score, 5))


def score_accuracy(score: int) ->int:
    return max(1, min(score, 5))


def score_reasoning(score: int) -> int:
    return max(1, min(score, 5))


def score_clarity(score: int) -> int:
    return max(1, min(score, 5))


def score_completeness(score: int) -> int:
    return max(1, min(score, 5))


def score_safety(score: int) -> int:
    return max(1, min(score, 5))


def overall_score(scores: Dict[str, int]) -> float:
    """Return the average score."""

    if not scores:
        return 0.0

    return round(sum(scores.values()) / len(scores), 2)


def score_response(response: str) -> Dict:
    """
    Example response scoring workflow.

    In a production system this function would analyze
    the response automatically.
    """

    scores = {
        "instruction_following": score_instruction_following(5),
        "accuracy": score_accuracy(4),
        "reasoning": score_reasoning(5),
        "clarity": score_clarity(4),
        "completeness": score_completeness(5),
        "safety": score_safety(5),
    }

    return {
        "scores": scores,
        "overall": overall_score(scores)
    }


if __name__ == "__main__":

    result = score_response("Sample LLM response")

    print(result)