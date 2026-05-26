# PCEP Quiz

Ein kleines Python-Quiz zur Vorbereitung auf PCEP/PCAP-Grundlagen.

---

## Projektbeschreibung

Dieses Programm stellt zufällige Python-Fragen, prüft die Antworten und zeigt am Ende eine Statistik an.

Das Ziel des Projekts ist es, ein funktionales Quiz-Programm zu entwickeln, das Fragen stellt, Antworten validiert und Ergebnisse auswertet.

---

## Features

- Zufällige Fragen
- Fragen-Datenbank in `questions.py`
- Antwortvalidierung mit `try/except`
- Punkte-System
- Erklärung nach jeder Frage
- Kategorie-Filter
- Schwierigkeits-Filter
- Statistik und Highscore
- Beste und schwächste Kategorie
- Menü-Steuerung
- Saubere Aufteilung in mehrere Dateien
- Unicode-Symbole (✓ ✗)

---

## Projektstruktur

```text
pcep-quiz/
├── main.py              # Hauptprogramm mit Menü-Loop
├── quiz_engine.py       # Kernfunktionen des Quiz
├── questions.py         # Fragen-Datenbank
├── stats.py             # Statistik und Highscore
├── README.md            # Dokumentation
└── .gitignore           # Optional
```

---

## Starten

```bash
python main.py
```

---

## Menü

```text
=== PCEP Quiz ===
1. Quiz starten
2. Quiz nach Kategorie starten
3. Quiz nach Schwierigkeit starten
4. Statistik anzeigen
5. Beenden
```

---

## Verwendete Konzepte

| Konzept | Verwendung im Projekt |
|---|---|
| Funktionen | Aufteilung in kleine Funktionen |
| Type Hints | Bessere Lesbarkeit und Codequalität |
| Listen | Speicherung mehrerer Fragen |
| Dictionaries | Speicherung einzelner Fragen und Ergebnisse |
| Schleifen | Menü-Loop und Quiz-Fragen |
| if/elif/else | Menü-Auswahl und Antwortprüfung |
| try/except | Fehlerbehandlung bei Eingaben |
| random.sample() | Zufällige Auswahl von Fragen |
| Imports | Aufteilung auf mehrere Dateien |
| f-Strings | Formatierte Ausgabe |

---

## Dateien

### main.py

Enthält das Hauptmenü und startet die verschiedenen Quiz-Modi.

Aufgaben von `main.py`:

- Menü anzeigen
- Normales Quiz starten
- Quiz nach Kategorie starten
- Quiz nach Schwierigkeit starten
- Statistik anzeigen
- Programm beenden

---

### quiz_engine.py

Enthält die Kernfunktionen für das Quiz.

Funktionen:

- `display_question()`
- `get_answer()`
- `check_answer()`
- `run_quiz()`
- `display_results()`

Aufgaben von `quiz_engine.py`:

- Fragen anzeigen
- Antwort einlesen
- Eingabe validieren
- Antwort prüfen
- Ergebnisse speichern
- Ergebnisübersicht anzeigen

---

### questions.py

Enthält alle Quizfragen als Liste von Dictionaries.

Jede Frage enthält:

- `question`
- `options`
- `correct_index`
- `explanation`
- `category`
- `difficulty`

---

### stats.py

Enthält Funktionen für:

- Statistik
- Highscore
- Beste Kategorie
- Schwächste Kategorie

Funktionen:

- `show_history()`
- `show_best_score()`
- `show_category_performance()`

Aufgaben von `stats.py`:

- Alle bisherigen Quiz-Ergebnisse anzeigen
- Besten Score anzeigen

---

## Beispiel-Frage

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

## Beispiel-Ablauf

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

## Statistik-Beispiel

```text
=== Statistik ===
1. Quiz: 4/5 richtig (80.0%)
2. Quiz: 3/5 richtig (60.0%)

=== Highscore ===
Bester Score: 4/5 (80.0%)
```

---

## Schwierigkeitsstufen

| Schwierigkeit | Bedeutung |
|---|---|
| 1 | Einfach |
| 2 | Mittel |
| 3 | Schwer |

---

## Kategorien

Beispiele für Kategorien:

- Datentypen
- Operatoren
- Kontrollstrukturen
- Syntax
- Exceptions
- Funktionen
- Module

---

## Anforderungen erfüllt

- Mindestens 10 Fragen
- Fragen als Liste von Dictionaries
- Verschiedene Kategorien
- Type Hints
- Eingabevalidierung mit `try/except`
- Menü mit mehreren Optionen
- Zufällige Fragen
- Statistik
- Kategorie-Filter
- Schwierigkeits-Filter
- Highscore
- Beste und schwächste Kategorie

---

## Autor

Alexandru Petrovici

Projekt erstellt im Rahmen der PCEP/PCAP Python-Übungen.