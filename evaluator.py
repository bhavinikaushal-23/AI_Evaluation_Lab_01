
def score_accuracy(response):
    text = response.lower()

    # Detect the specific incorrect claim in our example.
    if "at any time" in text and "after shipping" in text:
        return 0

    return 2


def score_completeness(response):
    text = response.lower()

    # A complete answer must explain the next step
    # after the order has shipped.
    if "return" in text and "after delivery" in text:
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
