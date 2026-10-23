
def score_accuracy(response):
    text = response.lower()
    incorrect_claims=[ "cancel your order at any time",
        "can cancel after shipping",
        "cancel even after shipping" ]
    for claim in incorrect_claims:
        if claim in text:
            return 0
    return 2


def score_completeness(response):
    text = response.lower()

    mentions_return = "return"
    mentions_after_delivery = ("after delivery" in text or "once delivered" in text)
    if mentions_return in text and mentions_after_delivery :
        return 2

    return 0


def evaluate_response(response):
    accuracy = score_accuracy(response)
    completeness = score_completeness(response)

    return {
        "factual_accuracy": accuracy,
        "completeness": completeness,
        "total_score": accuracy + completeness,
        "max_score": 4
    }
