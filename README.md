# PCEP Quiz

[🇬🇧 English](README.md) · [🇩🇪 Deutsch](README.de.md)

A command-line Python quiz application for practising core PCEP-level programming concepts.

The application loads questions from a JSON file, presents random quizzes, validates answers, explains each answer, and tracks quiz statistics for the current session.

> The current command-line interface and question bank are in German.

---

## Project Overview

PCEP Quiz is a modular Python learning project designed to practise fundamental programming concepts through interactive multiple-choice questions.

Users can start a random quiz, filter questions by category or difficulty, receive explanations after each answer, and review their performance through session-based statistics.

---

## Features

- Randomly selected quiz questions
- Question bank stored in `questions.json`
- Questions loaded from a JSON file
- Input validation with `try/except`
- Score tracking
- Explanation after every answer
- Category filter
- Difficulty filter
- Session statistics and high score
- Best and weakest category analysis
- Menu-based navigation
- Modular project structure across multiple files
- Unicode feedback symbols (`✓` and `✗`)
- 50+ Python quiz questions

---

## Requirements

- Python 3.10 or later
- No external packages required

---

## Project Structure

```text
pcep-quiz/
├── main.py
├── quiz_engine.py
├── stats.py
├── questions.json
├── questions_loader.py
├── README.md
├── README.de.md
└── .gitignore
```

---

## Run the Project

Clone the repository and move into the project directory:

```bash
git clone https://github.com/alexpetrovici/pcep-quiz.git
cd pcep-quiz
```

Then run:

```bash
python main.py
```

---

## Menu

```text
=== PCEP Quiz ===
1. Quiz starten
2. Quiz nach Kategorie starten
3. Quiz nach Schwierigkeit starten
4. Statistik anzeigen
5. Beenden
```

The menu currently supports:

1. Starting a random quiz
2. Starting a quiz filtered by category
3. Starting a quiz filtered by difficulty
4. Viewing statistics from the current session
5. Exiting the program

---

## Concepts Practised

| Concept | Use in the Project |
|---|---|
| Functions | Splitting program logic into focused functions |
| Type hints | Improving readability and expected data types |
| Lists | Storing collections of questions |
| Dictionaries | Representing questions, answers, and quiz results |
| Loops | Running the menu and processing quiz questions |
| `if` / `elif` / `else` | Handling menu choices and answer checks |
| `try` / `except` | Validating user input and handling invalid values |
| `random.sample()` | Selecting random questions without duplicates |
| Imports | Separating the application into multiple files |
| f-strings | Formatting terminal output |
| JSON | Loading quiz questions from an external file |

---

## Files

### `main.py`

Contains the main menu and controls the different quiz modes.

Responsibilities:

- Displaying the menu
- Starting a normal quiz
- Starting a category-filtered quiz
- Starting a difficulty-filtered quiz
- Displaying session statistics
- Closing the program

---

### `quiz_engine.py`

Contains the core quiz logic.

Functions:

- `display_question()`
- `get_answer()`
- `check_answer()`
- `run_quiz()`
- `display_results()`

Responsibilities:

- Displaying questions and answer options
- Reading and validating user input
- Checking answers
- Storing quiz results
- Displaying the final result summary
- Showing category performance for an individual quiz

---

### `questions.json`

Contains the complete question bank in JSON format.

Each question includes:

- `question`
- `options`
- `correct_index`
- `explanation`
- `category`
- `difficulty`

Example:

```python
{
    "question": "Welcher Datentyp ist 5.0?",
    "options": ["int", "float", "str", "bool"],
    "correct_index": 1,
    "explanation": "5.0 hat einen Dezimalpunkt, daher float.",
    "category": "Datentypen",
    "difficulty": 1
}
```

---

### `questions_loader.py`

Loads quiz questions from `questions.json`.

---

### `stats.py`

Contains session-statistics functions.

Functions:

- `show_history()`
- `show_best_score()`
- `show_category_performance()`

Responsibilities:

- Showing all completed quizzes from the current session
- Displaying the best score from the current session
- Identifying the strongest and weakest categories

> Results are stored only while the program is running. They reset when the application is closed.

---

## Example Quiz Flow

```text
=== PCEP Quiz ===
1. Quiz starten
2. Quiz nach Kategorie starten
3. Quiz nach Schwierigkeit starten
4. Statistik anzeigen
5. Beenden

Wahl (1-5): 1

Frage 1 von 5
----------------------------------------
Was gibt 2 ** 3 aus?
1. 6
2. 8
3. 9
4. Error

Deine Antwort: 2

✓ Richtig!
Erklärung: ** ist der Potenz-Operator.
```

---

## Example Statistics

```text
=== Statistik ===
1. Quiz: 4/5 richtig (80.0%)
2. Quiz: 3/5 richtig (60.0%)

=== Highscore ===
Bester Score: 4/5 (80.0%)
```

---

## Difficulty Levels

| Level | Meaning |
|---|---|
| 1 | Easy |
| 2 | Medium |
| 3 | Hard |

---

## Question Categories

Examples of included categories:

- Data types
- Operators
- Control structures
- Syntax
- Exceptions
- Functions
- Modules
- Lists
- Dictionaries
- String operations

---

## Future Ideas

- Save quiz history permanently in a `results.json` file
- Add automated tests
- Add an English-language CLI mode
- Allow users to choose the number of questions per quiz
- Add more advanced PCAP-level questions

---

## Author

Alexandru Petrovici

Created as part of PCEP/PCAP Python practice.
