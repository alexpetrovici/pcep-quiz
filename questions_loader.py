import json


def load_questions(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions