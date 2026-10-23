import json
from evaluator import evaluate_response

with open("test_cases.json","r",encoding="utf-8") as file:
    test_cases=json.load(file)

    passed=0
    failed=0

    for case in test_cases:
        case_id=case["case_id"]
        response=case["response"]
        expected_accuracy=case["expected_accuracy"]
        expected_completeness=case["expected_completeness"]
        result = evaluate_response(response)
        accuracy_matches=(result["factual_accuracy"]==expected_accuracy)
        completeness_matches=(result["completeness"]==expected_completeness)

        test_passed=accuracy_matches and completeness_matches
        if test_passed:
            passed+=1
        else:
            failed+=1

        print(f"\n TEST_CASE:{case_id}")
        print(f"Description : {case["description"]}")
        print(f"Actual Scores: {result}")
        print(f"Expected Accuracy: {expected_accuracy},"
              f"Expected Completeness:{expected_completeness}")
        print("Result: ","PASS" if test_passed else "FAIL")

    print("\n============EVALUATION SUMMARY ============")
    print(f"Total cases:{len(test_cases)}")
    print(f"Passed :{passed}")
    print(f"Failed:{failed} \n_________________________________________________________________")