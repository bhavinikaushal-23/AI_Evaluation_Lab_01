
from evaluator import evaluate_response


def test_bad_response():
    response = (
        "You can cancel your order at any time, "
        "even after shipping."
    )

    result = evaluate_response(response)

    assert result["factual_accuracy"] == 0
    assert result["completeness"] == 0


def test_good_response():
    response = (
        "You cannot cancel after shipping. "
        "Please request a return after delivery."
    )

    result = evaluate_response(response)

    assert result["factual_accuracy"] == 2
    assert result["completeness"] == 2
    assert result["total_score"] == 4
