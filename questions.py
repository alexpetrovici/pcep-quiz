questions = [
    {
        "question": "Welcher Datentyp ist 5.0?",
        "options": ["int", "float", "str", "bool"],
        "correct_index": 1,
        "explanation": "5.0 hat einen Dezimalpunkt, daher float.",
        "category": "Datentypen",
        "difficulty": 1
    },
    {
        "question": "Was gibt 3 // 2 aus?",
        "options": ["1", "1.5", "2", "Error"],
        "correct_index": 0,
        "explanation": "// ist Floor Division.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Welcher Wert ist vom Datentyp bool?",
        "options": ["'True'", "True", "1", "bool"],
        "correct_index": 1,
        "explanation": "True ohne Anführungszeichen ist ein bool-Wert.",
        "category": "Datentypen",
        "difficulty": 1
    },
    {
        "question": "Was gibt 2 ** 3 aus?",
        "options": ["6", "8", "9", "Error"],
        "correct_index": 1,
        "explanation": "** ist der Potenz-Operator.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Welche Schleife läuft, solange eine Bedingung wahr ist?",
        "options": ["for", "while", "if", "try"],
        "correct_index": 1,
        "explanation": "Eine while-Schleife läuft, solange die Bedingung True ist.",
        "category": "Kontrollstrukturen",
        "difficulty": 1
    },
    {
        "question": "Was bedeutet elif in Python?",
        "options": ["else if", "end loop if", "error if", "equal if"],
        "correct_index": 0,
        "explanation": "elif steht für else if.",
        "category": "Kontrollstrukturen",
        "difficulty": 1
    },
    {
        "question": "Wie erstellt man einen String korrekt?",
        "options": ["text = Hallo", "text = 'Hallo'", "text == 'Hallo'", "str Hallo"],
        "correct_index": 1,
        "explanation": "Strings stehen in Anführungszeichen.",
        "category": "Syntax",
        "difficulty": 1
    },
    {
        "question": "Welche Funktion gibt Text in der Konsole aus?",
        "options": ["input()", "print()", "str()", "int()"],
        "correct_index": 1,
        "explanation": "print() gibt Text oder Werte in der Konsole aus.",
        "category": "Syntax",
        "difficulty": 1
    },
    {
        "question": "Welche Exception entsteht oft bei int('abc')?",
        "options": ["TypeError", "NameError", "ValueError", "IndexError"],
        "correct_index": 2,
        "explanation": "ValueError entsteht, wenn ein Wert nicht passend umgewandelt werden kann.",
        "category": "Exceptions",
        "difficulty": 2
    },
    {
        "question": "Was macht input()?",
        "options": [
            "Es beendet das Programm",
            "Es liest eine Eingabe vom Nutzer",
            "Es zählt Listen",
            "Es importiert Module"
        ],
        "correct_index": 1,
        "explanation": "input() liest eine Eingabe vom Nutzer als String.",
        "category": "Funktionen",
        "difficulty": 1
    },
    {
        "question": "Was gibt len('Python') zurück?",
        "options": ["5", "6", "7", "Error"],
        "correct_index": 1,
        "explanation": "Das Wort Python hat 6 Zeichen.",
        "category": "Funktionen",
        "difficulty": 1
    },
    {
        "question": "Welcher Operator prüft Gleichheit?",
        "options": ["=", "==", "!=", ">="],
        "correct_index": 1,
        "explanation": "== prüft, ob zwei Werte gleich sind.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Was macht break in einer Schleife?",
        "options": [
            "Startet die Schleife neu",
            "Beendet die Schleife",
            "Überspringt alles",
            "Macht nichts"
        ],
        "correct_index": 1,
        "explanation": "break beendet die aktuelle Schleife sofort.",
        "category": "Kontrollstrukturen",
        "difficulty": 2
    },
    {
        "question": "Welcher Datentyp speichert mehrere Werte?",
        "options": ["list", "int", "bool", "float"],
        "correct_index": 0,
        "explanation": "Eine list kann mehrere Werte speichern.",
        "category": "Datentypen",
        "difficulty": 1
    },
    {
        "question": "Wie beginnt ein try/except Block?",
        "options": ["catch:", "try:", "except:", "error:"],
        "correct_index": 1,
        "explanation": "Ein Fehlerblock beginnt mit try:.",
        "category": "Exceptions",
        "difficulty": 2
    },
    {
        "question": "Was gibt type(5) zurück?",
        "options": ["float", "str", "int", "bool"],
        "correct_index": 2,
        "explanation": "5 ist ein Integer-Wert.",
        "category": "Funktionen",
        "difficulty": 1
    },
    {
        "question": "Welche Schleife wird oft mit range() verwendet?",
        "options": ["if", "while", "for", "try"],
        "correct_index": 2,
        "explanation": "for-Schleifen arbeiten oft mit range().",
        "category": "Kontrollstrukturen",
        "difficulty": 1
    },
    {
        "question": "Was macht continue in einer Schleife?",
        "options": [
            "Beendet das Programm",
            "Überspringt den aktuellen Durchlauf",
            "Löscht die Schleife",
            "Startet Python neu"
        ],
        "correct_index": 1,
        "explanation": "continue überspringt den aktuellen Schleifendurchlauf.",
        "category": "Kontrollstrukturen",
        "difficulty": 2
    },
    {
        "question": "Welcher Wert ist False in Python?",
        "options": ["True", "1", "False", "'False'"],
        "correct_index": 2,
        "explanation": "False ohne Anführungszeichen ist ein bool-Wert.",
        "category": "Datentypen",
        "difficulty": 1
    },
    {
        "question": "Was macht random.shuffle()?",
        "options": [
            "Sortiert eine Liste",
            "Mischt eine Liste zufällig",
            "Löscht Werte",
            "Verdoppelt Werte"
        ],
        "correct_index": 1,
        "explanation": "random.shuffle() mischt die Reihenfolge einer Liste.",
        "category": "Module",
        "difficulty": 2
    },
    {
        "question": "Was gibt 10 % 3 aus?",
        "options": ["1", "3", "0", "10"],
        "correct_index": 0,
        "explanation": "% gibt den Rest einer Division zurück. 10 geteilt durch 3 hat Rest 1.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Welcher Datentyp ist 'Hallo'?",
        "options": ["int", "float", "str", "bool"],
        "correct_index": 2,
        "explanation": "Text in Anführungszeichen ist ein String.",
        "category": "Datentypen",
        "difficulty": 1
    },
    {
        "question": "Was gibt bool(0) zurück?",
        "options": ["True", "False", "0", "Error"],
        "correct_index": 1,
        "explanation": "0 wird in Python als False bewertet.",
        "category": "Datentypen",
        "difficulty": 2
    },
    {
        "question": "Welche Funktion wandelt einen String in eine Zahl um?",
        "options": ["str()", "int()", "print()", "input()"],
        "correct_index": 1,
        "explanation": "int() kann einen passenden String in eine ganze Zahl umwandeln.",
        "category": "Funktionen",
        "difficulty": 1
    },
    {
        "question": "Was gibt 'Py' + 'thon' aus?",
        "options": ["Py thon", "Python", "Error", "Py+thon"],
        "correct_index": 1,
        "explanation": "Mit + können Strings verbunden werden.",
        "category": "String Ops",
        "difficulty": 1
    },
    {
        "question": "Was gibt 'ha' * 3 aus?",
        "options": ["hahaha", "ha3", "Error", "ha ha ha"],
        "correct_index": 0,
        "explanation": "Strings können mit * mehrfach wiederholt werden.",
        "category": "String Ops",
        "difficulty": 1
    },
    {
        "question": "Was prüft der Operator !=",
        "options": ["Gleichheit", "Ungleichheit", "Größer als", "Kleiner als"],
        "correct_index": 1,
        "explanation": "!= prüft, ob zwei Werte ungleich sind.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Welche Bedingung ist True?",
        "options": ["5 < 3", "5 == 3", "5 > 3", "5 != 5"],
        "correct_index": 2,
        "explanation": "5 ist größer als 3, daher ist 5 > 3 True.",
        "category": "Operatoren",
        "difficulty": 1
    },
    {
        "question": "Was macht range(5)?",
        "options": ["Erzeugt Zahlen von 1 bis 5", "Erzeugt Zahlen von 0 bis 4", "Erzeugt nur die 5", "Erzeugt einen String"],
        "correct_index": 1,
        "explanation": "range(5) erzeugt die Werte 0, 1, 2, 3, 4.",
        "category": "Kontrollstrukturen",
        "difficulty": 1
    },
    {
        "question": "Was passiert bei einer if-Bedingung?",
        "options": ["Code wird immer ausgeführt", "Code wird nur bei True ausgeführt", "Code wird nie ausgeführt", "Python beendet sich"],
        "correct_index": 1,
        "explanation": "Ein if-Block wird ausgeführt, wenn die Bedingung True ist.",
        "category": "Kontrollstrukturen",
        "difficulty": 1
    },
    {
        "question": "Welche Schreibweise ist für eine Funktion korrekt?",
        "options": ["function test():", "def test():", "func test():", "test def():"],
        "correct_index": 1,
        "explanation": "Funktionen werden in Python mit def definiert.",
        "category": "Syntax",
        "difficulty": 1
    },
    {
        "question": "Was bedeutet return in einer Funktion?",
        "options": ["Es beendet Python", "Es gibt einen Wert zurück", "Es startet eine Schleife", "Es importiert ein Modul"],
        "correct_index": 1,
        "explanation": "return gibt einen Wert aus der Funktion zurück.",
        "category": "Funktionen",
        "difficulty": 1
    },
    {
        "question": "Welche Exception entsteht oft bei einer Division durch 0?",
        "options": ["ValueError", "ZeroDivisionError", "NameError", "TypeError"],
        "correct_index": 1,
        "explanation": "Eine Division durch 0 erzeugt einen ZeroDivisionError.",
        "category": "Exceptions",
        "difficulty": 2
    },
    {
        "question": "Was passiert bei print(name), wenn name nicht definiert wurde?",
        "options": ["ValueError", "NameError", "IndexError", "SyntaxError"],
        "correct_index": 1,
        "explanation": "Wenn eine Variable nicht existiert, entsteht ein NameError.",
        "category": "Exceptions",
        "difficulty": 2
    },
    {
        "question": "Was gibt [1, 2, 3][0] zurück?",
        "options": ["1", "2", "3", "0"],
        "correct_index": 0,
        "explanation": "Listen-Indizes starten bei 0. Der erste Wert ist 1.",
        "category": "Listen",
        "difficulty": 2
    },
    {
        "question": "Was macht append() bei einer Liste?",
        "options": ["Es löscht die Liste", "Es fügt ein Element hinzu", "Es sortiert die Liste", "Es wandelt die Liste in Text um"],
        "correct_index": 1,
        "explanation": "append() fügt ein neues Element am Ende einer Liste hinzu.",
        "category": "Listen",
        "difficulty": 1
    },
    {
        "question": "Was gibt len([1, 2, 3]) zurück?",
        "options": ["2", "3", "4", "Error"],
        "correct_index": 1,
        "explanation": "Die Liste enthält drei Elemente.",
        "category": "Listen",
        "difficulty": 1
    },
    {
        "question": "Wie greift man auf den Wert eines Dictionaries zu?",
        "options": ["dict.value", "dict['key']", "dict(key)", "dict->key"],
        "correct_index": 1,
        "explanation": "Auf Dictionary-Werte greift man mit dem Schlüssel in eckigen Klammern zu.",
        "category": "Dictionaries",
        "difficulty": 2
    },
    {
        "question": "Was macht random.sample(questions, 5)?",
        "options": ["Es löscht 5 Fragen", "Es wählt 5 zufällige Fragen ohne Dopplung", "Es sortiert 5 Fragen", "Es erstellt 5 neue Fragen"],
        "correct_index": 1,
        "explanation": "random.sample() wählt eine bestimmte Anzahl zufälliger Elemente ohne Dopplung aus.",
        "category": "Module",
        "difficulty": 2
    },
    {
        "question": "Was ist ein Type Hint?",
        "options": ["Ein Kommentar für Farben", "Ein Hinweis auf erwartete Datentypen", "Ein Fehler im Code", "Eine Schleife"],
        "correct_index": 1,
        "explanation": "Type Hints zeigen an, welche Datentypen erwartet oder zurückgegeben werden.",
        "category": "Syntax",
        "difficulty": 2
    },
    {
        "question": "Was gibt 3 == '3' zurück?",
        "options": ["True", "False", "3", "Error"],
        "correct_index": 1,
        "explanation": "3 ist ein int, '3' ist ein str. Sie sind nicht gleich.",
        "category": "Datentypen",
        "difficulty": 2
    },
    {
        "question": "Was bedeutet and in einer Bedingung?",
        "options": ["Mindestens eine Bedingung muss True sein", "Alle Bedingungen müssen True sein", "Keine Bedingung darf True sein", "Es beendet die Bedingung"],
        "correct_index": 1,
        "explanation": "Bei and müssen alle Teilbedingungen True sein.",
        "category": "Operatoren",
        "difficulty": 2
    },
    {
        "question": "Was bedeutet or in einer Bedingung?",
        "options": ["Alle Bedingungen müssen True sein", "Mindestens eine Bedingung muss True sein", "Es vergleicht Zahlen", "Es erstellt eine Liste"],
        "correct_index": 1,
        "explanation": "Bei or reicht es, wenn eine Teilbedingung True ist.",
        "category": "Operatoren",
        "difficulty": 2
    },
    {
        "question": "Was gibt not True zurück?",
        "options": ["True", "False", "None", "Error"],
        "correct_index": 1,
        "explanation": "not kehrt einen bool-Wert um.",
        "category": "Operatoren",
        "difficulty": 2
    },
    {
        "question": "Welche Aussage über input() ist richtig?",
        "options": ["input() gibt immer int zurück", "input() gibt immer str zurück", "input() gibt immer bool zurück", "input() gibt nichts zurück"],
        "correct_index": 1,
        "explanation": "input() gibt die Eingabe standardmäßig als String zurück.",
        "category": "Funktionen",
        "difficulty": 2
    },
    {
        "question": "Was ist der Index des ersten Elements in einer Liste?",
        "options": ["0", "1", "-1", "first"],
        "correct_index": 0,
        "explanation": "Python-Listen beginnen beim Index 0.",
        "category": "Listen",
        "difficulty": 1
    },
    {
        "question": "Was gibt [1, 2, 3][-1] zurück?",
        "options": ["1", "2", "3", "Error"],
        "correct_index": 2,
        "explanation": "Der Index -1 greift auf das letzte Element einer Liste zu.",
        "category": "Listen",
        "difficulty": 2
    },
    {
        "question": "Was macht .strip() bei einem String?",
        "options": ["Es löscht alle Buchstaben", "Es entfernt Leerzeichen am Anfang und Ende", "Es wandelt Text in Zahlen um", "Es teilt einen String"],
        "correct_index": 1,
        "explanation": ".strip() entfernt Leerzeichen am Anfang und Ende eines Strings.",
        "category": "String Ops",
        "difficulty": 2
    },
    {
        "question": "Was macht .split(' ')?",
        "options": ["Es verbindet Strings", "Es teilt einen String an Leerzeichen", "Es löscht Leerzeichen", "Es sortiert Wörter"],
        "correct_index": 1,
        "explanation": ".split(' ') teilt einen String an Leerzeichen in eine Liste.",
        "category": "String Ops",
        "difficulty": 2
    },
    {
        "question": "Was macht ein import in Python?",
        "options": ["Es löscht ein Modul", "Es lädt Code aus einem Modul", "Es beendet das Programm", "Es erstellt automatisch eine Funktion"],
        "correct_index": 1,
        "explanation": "Mit import kann man Funktionen, Variablen oder Module aus anderen Dateien verwenden.",
        "category": "Module",
        "difficulty": 1
    },
    {
        "question": "Welche Schreibweise ist ein gültiger Type Hint für eine Funktion ohne Rückgabewert?",
        "options": ["-> none", "-> None", "=> None", ": None"],
        "correct_index": 1,
        "explanation": "Für keinen Rückgabewert verwendet man -> None.",
        "category": "Syntax",
        "difficulty": 2
    },
    {
        "question": "Was passiert bei einer SyntaxError?",
        "options": ["Python versteht den Code nicht", "Eine Zahl ist zu groß", "Eine Liste ist leer", "Ein Modul fehlt"],
        "correct_index": 0,
        "explanation": "Ein SyntaxError entsteht, wenn der Code nicht korrekt geschrieben ist.",
        "category": "Exceptions",
        "difficulty": 2
    },
    {
        "question": "Was macht list.copy()?",
        "options": ["Es löscht die Liste", "Es erstellt eine Kopie der Liste", "Es sortiert die Liste", "Es zählt die Elemente"],
        "correct_index": 1,
        "explanation": "copy() erstellt eine neue Kopie einer Liste.",
        "category": "Listen",
        "difficulty": 2
    },
    {
        "question": "Was ist bei einem Dictionary eindeutig?",
        "options": ["Die Werte", "Die Schlüssel", "Die Reihenfolge", "Die Kommentare"],
        "correct_index": 1,
        "explanation": "Dictionary-Schlüssel müssen eindeutig sein.",
        "category": "Dictionaries",
        "difficulty": 2
    },
    {
        "question": "Was macht dictionary.items()?",
        "options": ["Es gibt Schlüssel-Wert-Paare zurück", "Es löscht alle Werte", "Es sortiert das Dictionary", "Es gibt nur Schlüssel zurück"],
        "correct_index": 0,
        "explanation": ".items() liefert Schlüssel-Wert-Paare eines Dictionaries.",
        "category": "Dictionaries",
        "difficulty": 2
    },
    {
        "question": "Was macht dictionary.keys()?",
        "options": ["Es gibt alle Werte zurück", "Es gibt alle Schlüssel zurück", "Es löscht Schlüssel", "Es erstellt ein neues Dictionary"],
        "correct_index": 1,
        "explanation": ".keys() gibt die Schlüssel eines Dictionaries zurück.",
        "category": "Dictionaries",
        "difficulty": 1
    },
    {
        "question": "Was macht dictionary.values()?",
        "options": ["Es gibt alle Werte zurück", "Es gibt alle Schlüssel zurück", "Es löscht Werte", "Es prüft Fehler"],
        "correct_index": 0,
        "explanation": ".values() gibt die Werte eines Dictionaries zurück.",
        "category": "Dictionaries",
        "difficulty": 1
    },
    {
        "question": "Was ist der Unterschied zwischen = und ==?",
        "options": ["Keiner", "= weist zu, == vergleicht", "= vergleicht, == weist zu", "Beide löschen Werte"],
        "correct_index": 1,
        "explanation": "= weist einen Wert zu, == vergleicht zwei Werte.",
        "category": "Operatoren",
        "difficulty": 2
    },
    {
        "question": "Was macht eine Funktion modular?",
        "options": ["Sie ist sehr lang", "Sie erfüllt eine klare Aufgabe", "Sie enthält keine Namen", "Sie enthält keine Parameter"],
        "correct_index": 1,
        "explanation": "Eine gute Funktion erfüllt eine klare, einzelne Aufgabe.",
        "category": "Funktionen",
        "difficulty": 3
    },
    {
        "question": "Warum sollte man keine riesigen Funktionen schreiben?",
        "options": ["Weil Python sie nicht startet", "Weil sie schwer zu lesen und zu testen sind", "Weil sie immer langsamer sind", "Weil Type Hints dann nicht funktionieren"],
        "correct_index": 1,
        "explanation": "Kurze Funktionen sind besser lesbar, testbar und wartbar.",
        "category": "Funktionen",
        "difficulty": 3
    },
    {
        "question": "Was ist ein möglicher Nachteil von except Exception?",
        "options": ["Es fängt zu viele Fehler ab", "Es funktioniert nie", "Es löscht Variablen", "Es beendet Schleifen"],
        "correct_index": 0,
        "explanation": "except Exception kann Fehler verstecken, die man eigentlich sehen sollte.",
        "category": "Exceptions",
        "difficulty": 3
    },
    {
        "question": "Was gibt bool('False') zurück?",
        "options": ["True", "False", "Error", "None"],
        "correct_index": 0,
        "explanation": "Ein nicht-leerer String ist in Python True, auch wenn der Text 'False' ist.",
        "category": "Datentypen",
        "difficulty": 3
    },
    {
        "question": "Was gibt 5 / 2 aus?",
        "options": ["2", "2.5", "3", "Error"],
        "correct_index": 1,
        "explanation": "/ führt eine normale Division aus und gibt einen float zurück.",
        "category": "Operatoren",
        "difficulty": 3
    },
    {
        "question": "Was gibt 5 // 2 aus?",
        "options": ["2", "2.5", "3", "Error"],
        "correct_index": 0,
        "explanation": "// ist Floor Division und gibt bei positiven Zahlen den ganzzahligen Anteil zurück.",
        "category": "Operatoren",
        "difficulty": 3
    },
    {
        "question": "Was gibt len('') zurück?",
        "options": ["0", "1", "None", "Error"],
        "correct_index": 0,
        "explanation": "Ein leerer String enthält 0 Zeichen.",
        "category": "String Ops",
        "difficulty": 3
    },
    {
        "question": "Was gibt 'Python'[0] zurück?",
        "options": ["P", "y", "0", "Python"],
        "correct_index": 0,
        "explanation": "Strings können wie Listen indexiert werden. Index 0 ist das erste Zeichen.",
        "category": "String Ops",
        "difficulty": 3
    },
    {
        "question": "Was gibt 'Python'[-1] zurück?",
        "options": ["P", "n", "Error", "-1"],
        "correct_index": 1,
        "explanation": "Index -1 greift auf das letzte Zeichen zu.",
        "category": "String Ops",
        "difficulty": 3
    },
    {
        "question": "Was passiert, wenn eine Funktion kein return hat?",
        "options": ["Sie gibt automatisch None zurück", "Sie gibt 0 zurück", "Sie erzeugt immer einen Fehler", "Sie wird nicht ausgeführt"],
        "correct_index": 0,
        "explanation": "Wenn kein return vorhanden ist, gibt eine Python-Funktion automatisch None zurück.",
        "category": "Funktionen",
        "difficulty": 3
    },
    {
        "question": "Was ist der Unterschied zwischen print() und return?",
        "options": ["Keiner", "print() zeigt etwas an, return gibt einen Wert zurück", "return zeigt Text an", "print() beendet eine Funktion"],
        "correct_index": 1,
        "explanation": "print() gibt etwas in der Konsole aus, return liefert einen Wert an den Aufrufer zurück.",
        "category": "Funktionen",
        "difficulty": 3
    },
    {
        "question": "Was gibt [1, 2, 3][1] zurück?",
        "options": ["1", "2", "3", "Error"],
        "correct_index": 1,
        "explanation": "Listen starten bei Index 0. Index 1 ist das zweite Element.",
        "category": "Listen",
        "difficulty": 3
    },
    {
        "question": "Was passiert bei [1, 2, 3][5]?",
        "options": ["5", "None", "IndexError", "ValueError"],
        "correct_index": 2,
        "explanation": "Index 5 existiert in dieser Liste nicht, daher entsteht ein IndexError.",
        "category": "Exceptions",
        "difficulty": 3
    },
    {
        "question": "Was macht eine verschachtelte Schleife?",
        "options": ["Eine Schleife innerhalb einer Schleife", "Eine Schleife ohne Bedingung", "Eine Funktion ohne return", "Ein Dictionary ohne Schlüssel"],
        "correct_index": 0,
        "explanation": "Bei einer verschachtelten Schleife befindet sich eine Schleife innerhalb einer anderen Schleife.",
        "category": "Kontrollstrukturen",
        "difficulty": 3
    },
    {
        "question": "Was gibt {'a': 1}['a'] zurück?",
        "options": ["a", "1", "Error", "None"],
        "correct_index": 1,
        "explanation": "Mit dem Schlüssel 'a' greift man auf den Wert 1 zu.",
        "category": "Dictionaries",
        "difficulty": 3
    },
    {
        "question": "Was passiert bei {'a': 1}['b']?",
        "options": ["0", "None", "KeyError", "ValueError"],
        "correct_index": 2,
        "explanation": "Der Schlüssel 'b' existiert nicht, daher entsteht ein KeyError.",
        "category": "Exceptions",
        "difficulty": 3
    },
    {
        "question": "Was bedeutet mutable?",
        "options": ["Veränderbar", "Unveränderbar", "Fehlerhaft", "Zufällig"],
        "correct_index": 0,
        "explanation": "Mutable bedeutet, dass ein Objekt nach der Erstellung verändert werden kann, z.B. eine Liste.",
        "category": "Datentypen",
        "difficulty": 3
    },
    {
        "question": "Welcher Datentyp ist mutable?",
        "options": ["str", "int", "list", "bool"],
        "correct_index": 2,
        "explanation": "Listen sind mutable, also veränderbar.",
        "category": "Datentypen",
        "difficulty": 3
    }
]