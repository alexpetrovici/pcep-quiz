from questions import questions
import quiz_engine
import random
import stats


def get_categories() -> list[str]:
    categories = []

    for question in questions:
        category = question["category"]

        if category not in categories:
            categories.append(category)

    return categories


def get_difficulties() -> list[int]:
    difficulties = []

    for question in questions:
        difficulty = question["difficulty"]

        if difficulty not in difficulties:
            difficulties.append(difficulty)

    return difficulties


def choose_category() -> list[dict]:
    categories = get_categories()

    print("\n=== Kategorien ===")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    try:
        choice = int(input("\nKategorie wählen: "))

        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]

            return [ question for question in questions if question["category"] == selected_category ]

        print("Ungültige Kategorie!")

    except ValueError:
        print("Bitte eine Zahl eingeben!")

    return []


def choose_difficulty() -> list[dict]:
    difficulties = get_difficulties()

    print("\n=== Schwierigkeit ===")

    for difficulty in difficulties:
        if difficulty == 1:
            name = "Einfach"
        elif difficulty == 2:
            name = "Mittel"
        elif difficulty == 3:
            name = "Schwer"
        else:
            name = "Unbekannt"

        print(f"{difficulty}. {name}")

    try:
        choice = int(input("\nSchwierigkeit wählen: "))


        return [ question for question in questions if question["difficulty"] == choice ]

    except ValueError:
        print("Bitte eine Zahl eingeben!")

    return []


def start_quiz(quiz_questions: list[dict], all_results: list[dict]) -> None:
    if not quiz_questions:
        print("Keine Fragen gefunden!")
        return

    amount = min(5, len(quiz_questions))
    selected_questions = random.sample(quiz_questions, amount)

    results = quiz_engine.run_quiz(selected_questions)
    quiz_engine.display_results(results)
    all_results.append(results)


def main() -> None:
    all_results: list[dict] = []

    print("=" * 40)
    print("Willkommen zum PCEP Quiz!")
    print("=" * 40)

    while True:
        print("\n=== PCEP Quiz ===")
        print("1. Quiz starten")
        print("2. Quiz nach Kategorie starten")
        print("3. Quiz nach Schwierigkeit starten")
        print("4. Statistik anzeigen")
        print("5. Beenden")

        choice = input("\nWahl (1-5): ").strip()

        if choice == "1":
            start_quiz(questions, all_results)

        elif choice == "2":
            category_questions = choose_category()
            start_quiz(category_questions, all_results)

        elif choice == "3":
            difficulty_questions = choose_difficulty()
            start_quiz(difficulty_questions, all_results)

        elif choice == "4":
            stats.show_history(all_results)
            stats.show_best_score(all_results)
            stats.show_category_performance(all_results)

        elif choice == "5":
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültig! Bitte 1-5 eingeben.")


if __name__ == "__main__":
    main()