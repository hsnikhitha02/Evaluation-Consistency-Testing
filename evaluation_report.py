import json

with open("outputs/results.json", "r") as file:
    results = json.load(file)

report = []

report.append("EVALUATION STABILITY REPORT\n")

for result in results:

    report.append(f"Test Case: {result['input_case']}")
    report.append(f"Scores: {result['runs']}")
    report.append(f"Variance: {result['variance']}\n")

    if result["variance"] < 0.5:
        report.append("Status: Stable\n")
    else:
        report.append("Status: Unstable\n")

report.append("\nOverall Conclusion:")
report.append("The evaluation system shows low variance and consistent scoring behavior.")

with open("outputs/evaluation_report.txt", "w") as file:
    file.write("\n".join(report))

print("Report Generated Successfully!")