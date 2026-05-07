import json
import statistics

from evaluator import evaluate_answer

# Load dataset
with open("dataset/test_cases.json", "r") as file:
    test_cases = json.load(file)

final_results = []

# Run tests
for case in test_cases:

    scores = []

    # Repeat same test 5 times
    for i in range(5):

        score = evaluate_answer(
            case["question"],
            case["answer"]
        )

        scores.append(score)

    # Calculate variance
    variance = round(statistics.variance(scores), 3)

    result = {
        "input_case": case["type"],
        "question": case["question"],
        "runs": scores,
        "variance": variance
    }

    final_results.append(result)

# Save results
with open("outputs/results.json", "w") as file:
    json.dump(final_results, file, indent=4)

print("Testing Completed Successfully!")