def show_history(all_results: list[dict]) -> None:
    if not all_results:
        print("Noch keine Quizze gemacht!")
        return

    print("\n=== Statistik ===")

    for i, result in enumerate(all_results, 1):
        percentage = (result["correct"] / result["total"]) * 100
        print(f"{i}. Quiz: {result['correct']}/{result['total']} richtig ({percentage:.1f}%)")


def show_best_score(all_results: list[dict]) -> None:
    if not all_results:
        return

    best_result = all_results[0]

    for result in all_results:
        if result["correct"] > best_result["correct"]:
            best_result = result

    percentage = (best_result["correct"] / best_result["total"]) * 100

    print("\n=== Highscore ===")
    print(f"Bester Score: {best_result['correct']}/{best_result['total']} ({percentage:.1f}%)")


def show_category_performance(all_results: list[dict]) -> None:
    if not all_results:
        return

    categories: dict = {}

    for result in all_results:
        for detail in result["details"]:
            category = detail["category"]

            if category not in categories:
                categories[category] = {
                    "correct": 0,
                    "total": 0
                }

            categories[category]["total"] += 1

            if detail["correct"]:
                categories[category]["correct"] += 1

    best_category: str | None = None
    worst_category: str | None = None
    best_percentage = -1
    worst_percentage = 101

    for category, data in categories.items():
        percentage = (data["correct"] / data["total"]) * 100

        if percentage > best_percentage:
            best_percentage = percentage
            best_category = category

        if percentage < worst_percentage:
            worst_percentage = percentage
            worst_category = category

    print("\n=== Beste/Schwächste Kategorie ===")
    print(f"Beste Kategorie: {best_category} ({best_percentage:.1f}%)")
    print(f"Schwächste Kategorie: {worst_category} ({worst_percentage:.1f}%)")