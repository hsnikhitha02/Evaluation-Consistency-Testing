import random

def evaluate_answer(question, answer):

    answer = answer.lower()

    # Simulated AI scoring

    if "subset of ai" in answer:
        score = random.uniform(8.5, 9.5)

    elif "computers learn" in answer:
        score = random.uniform(5.0, 7.0)

    elif "cooking" in answer:
        score = random.uniform(1.0, 3.0)

    else:
        score = random.uniform(0.0, 1.5)

    return round(score, 2)