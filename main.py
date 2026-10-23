from evaluator import evaluate_response

ai_response= "You can cancel your order at any time, even after shipping."

reference_policy=("Orders can be cancelled before shipping. "
                "After shipping, the customer must request a return after delivery.")

print("AI Response : ",ai_response)
print("Reference policy:", reference_policy)

RESULT=evaluate_response(ai_response)
print("Evaluation Result= ",RESULT)