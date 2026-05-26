def display_question(question: dict, num: int, total: int) -> None:
    print(f"\nFrage {num} von {total}")
    print("-" * 40)
    print(question["question"])

    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")


def get_answer(question: dict) -> int:
    while True:
        try:
            answer = int(input("Deine Antwort: "))

            if 1 <= answer <= len(question["options"]):
                return answer

            print(f"Bitte eine Zahl zwischen 1 und {len(question['options'])} eingeben.")

        except ValueError:
            print("Fehler: Bitte eine Zahl eingeben!")


def check_answer(answer: int, question: dict) -> bool:
    return answer - 1 == question["correct_index"]


def run_quiz(questions: list[dict]) -> dict:
    results = {
        "total": len(questions),
        "correct": 0,
        "wrong": 0,
        "details": []
    }

    for i, question in enumerate(questions, 1):
        display_question(question, i, len(questions))
        answer = get_answer(question)
        is_correct = check_answer(answer, question)

        if is_correct:
            print("\n✓ Richtig!")
            results["correct"] += 1
        else:
            print("\n✗ Falsch!")
            results["wrong"] += 1

        print(f"Erklärung: {question['explanation']}")

        results["details"].append({
            "question": question["question"],
            "correct": is_correct,
            "category": question["category"]
        })

    return results


def display_results(results: dict) -> None:
    percentage = (results["correct"] / results["total"]) * 100

    print("\n" + "=" * 40)
    print("Quiz beendet!")
    print(f"Richtig: {results['correct']}")
    print(f"Falsch: {results['wrong']}")
    print(f"Gesamt: {results['total']}")
    print(f"Prozent: {percentage:.1f}%")

    categories: dict = {}

    for detail in results["details"]:
        category = detail["category"]

        if category not in categories:
            categories[category] = {
                "correct": 0,
                "total": 0
            }

        categories[category]["total"] += 1

        if detail["correct"]:
            categories[category]["correct"] += 1

    print("\nKategorie-Statistik:")

    for category, stats in categories.items():
        print(
            f"{category}: "
            f"{stats['correct']}/{stats['total']} richtig"
        )

    print("=" * 40)