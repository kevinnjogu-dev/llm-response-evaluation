from src.scoring import score_response, overall_score


def test_score_response():
    result = score_response("Test response")

    assert "scores" in result
    assert "overall" in result
    assert result["overall"] > 0


def test_overall_score():
    scores = {
        "accuracy": 5,
        "clarity": 5
    }

    assert overall_score(scores) == 5.0