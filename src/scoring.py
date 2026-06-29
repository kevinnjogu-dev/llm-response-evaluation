"""
LLM Response Scoring Module

This module provides functions for evaluating Large Language Model
responses across several quality dimensions.
"""

from typing import Dict


def score_instruction_following(score: int) -> int:
    """Score how well the model followed the prompt."""
    return max(1, min(score, 5))


def score_accuracy(score: int) -> int:
    """Score factual correctness."""
    return max(1, min(score, 5))


def score_reasoning(score: int) -> int:
    """Score logical reasoning."""
    return max(1, min(score, 5))


def score_clarity(score: int) -> int:
    """Score readability and clarity."""
    return max(1, min(score, 5))


def score_completeness(score: int) -> int:
    """Score completeness of the response."""
    return max(1, min(score, 5))


def score_safety(score: int) -> int:
    """Score safety and harmlessness."""
    return max(1, min(score, 5))


def overall_score(scores: Dict[str, int]) -> float:
    """
    Calculate the average evaluation score.
    """

    if not scores:
        return 0.0

    return round(sum(scores.values()) / len(scores), 2)


if __name__ == "__main__":

    evaluation = {
        "instruction_following": 5,
        "accuracy": 4,
        "reasoning": 5,
        "clarity": 4,
        "completeness": 5,
        "safety": 5,
    }

    print("Overall Score:", overall_score(evaluation))