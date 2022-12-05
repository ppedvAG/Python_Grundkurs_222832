# List
# Kann mehrere Werte enthalten und diese in einer Variable speichern
# Hat einen Index wie String
# Ist veränderbar, es können neue Elemente hinzugefügt werden oder bestehende entfernt werden
# Duplikate sind erlaubt
# Verschiedene Datentypen sind erlaubt, aber nicht empfohlen

meineListe = [1, 2, 3, 4, 'Text', True]
print(meineListe)  # Liste kann einfach mit print ausgegeben werden

# Kann auf einzelne Werte zugreifen mittels Index
print(meineListe[4])  # Index hier auch wieder 0-basiert -> Ausgabe: Text
print(meineListe[1:4])  # Range hier auch möglich
print(meineListe[-1])  # Auch von rechts die Liste angreifbar

# list(Objekt)
# Wandelt das Objekt in eine Liste um (wenn möglich)
text = "Ein Text"
stringListe = list(text)
print(stringListe)  # Jedes Zeichen im String ist jetzt ein Element in der Liste
print(stringListe[1])

# list.append(Element)
# Hängt ein Element an das Ende der Liste an
meineListe.append("Abc")
print(meineListe)

meineListe.append(stringListe)  # Liste als letztes Element anhängen (verschachtelte Liste)
print(meineListe)

print(meineListe[-1][0])  # Verschachtelte Liste mit zwei Indizes angreifen

# list.extend(Liste)
# Hängt alle Elemente der gegebenen Liste an die Liste an
meineListe.extend(stringListe)
print(meineListe)  # Jedes Element der stringListe ist jetzt ein neues Element
print(len(meineListe))  # 16

# list.pop(Index)
# Entfernt ein Element an einer bestimmten Stelle
# Gibt das entfernte Element zurück
entferntesElement = meineListe.pop(7)
print(meineListe)  # Liste entfernt
print(entferntesElement)

# list.remove(Wert)
# Sucht nach einem Wert in der Liste und entfernt ihn
meineListe.append('E')
meineListe.remove('E')
print(meineListe)  # Nur das erste E wird entfernt

# list.clear()
# Entleert die Liste
meineListe.clear()
print(meineListe)

# list.sort()
# Sortiert die Liste
# Standardmäßig Alphanumerisch
# Funktioniert nicht mit gemischten Listen
meineListe.sort()
print(meineListe)

# Tuple
# Verhalten sich ähnlich wie Listen
# Sind nicht veränderbar, keine neuen Elemente, bestehende Elemente können nicht verändert werden
# Duplikate sind erlaubt
# Datentypen können auch gemischt sein
# Index vorhanden
# Verschachtelbar
meinTuple = (1, 2, 3, 4)
print(meinTuple)

# Workaround um Werte im Tupel zu verändern
meinTuple = list(meinTuple)
meinTuple[0] = 10
meinTuple = tuple(meinTuple)  # tuple Funktion genau wie list Funktion
print(meinTuple)

# Unpacking
# Löst iterierbare Objekte in ihre einzelnen Elemente auf und danach auf Variablen zuweisen
# Anzahl der Variablen = Anzahl der Inhalte
# Funktioniert bei List, Tuple, String, ...
unpacking = [1, 2, 3, 4]
(eins, zwei, drei, vier) = unpacking  # Vier Variablen definieren, einzelne Elemente stehen dann in den einzelnen Variablen
print(eins)
print(vier)

# Range
# Gibt eine nichtveränderbare Sequenz von Integern
# Werden häufig in Listen umgewandelt

# Syntax
# range(Endzahl) -> Sequenz von 0 bis <Endzahl>
# range(100) -> Sequenz von 0-99
# Obergrenze ist exkludiert
# Untergrenze ist inkludiert
meineRange = range(100)
print(meineRange)  # Gibt die Range nicht aus
print(list(meineRange))  # Gibt die Range als Liste aus

# range(<Startzahl>, <Endzahl>) -> Sequenz aus <Startzahl> - <Endzahl>
# range(50, 100) -> Sequenz von 50-99
print(list(range(50, 100)))

# range(<Startzahl>, <Endzahl>, <Schrittgröße>) -> Sequenz aus <Startzahl> - <Endzahl> mit <Schrittgröße> großen Schritten aber nur bis unter die Obergrenze
print(list(range(0, 100, 5)))  # 100 nicht dabei, da Obergrenze exkludiert
print(list(range(0, 101, 5)))  # 100 dabei, +1 um Obergrenze zu inkludieren

# Set
# Funktioniert ähnlich wie Liste
# Kein Index -> keine Anpassungen bei vorhandenen Werten
# Keine Duplikate
# Werte können hinzugefügt und entfernt werden
meinSet = {1, 2, 3, 4, 5}
print(meinSet)

# set.add(Element)
# Fügt ein Element am Ende des Sets hinzu
meinSet.add(6)
meinSet.add(6)  # Fügt Duplikate kein weiteres mal hinzu
print(meinSet)

# set.pop()
# Entfernt das erste Element
meinSet.pop()
print(meinSet)

# set.update(Liste)
# Alle Elemente aus der Liste in das Set einfügen die nicht vorhanden sind
meinSet.update(meinTuple)
print(meinSet)

# Liste mit Duplikaten einzigartig machen über Set
eindeutig = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5]
eindeutig = set(eindeutig)  # Set Funktion für Konvertierung
eindeutig = list(eindeutig)
print(eindeutig)

# Dictionary
# Liste von Key-Value Paaren
# Sind veränderbar
# Keine Key-Duplikate
meinCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

print(meinCar)
print(meinCar["Year"])  # 2017

# Werte verändern
meinCar["Year"] = 2018
print(meinCar)

# Weiteren Wert hinzufügen
meinCar["KM"] = 50000
print(meinCar)

# dictionary.setdefault("key", Wert)
# Füge den Eintrag hinzu wenn er nicht existiert
# Falls der Eintrag existiert wird der Wert zurückgegeben
meinCar.setdefault("Wheels", 4)  # Fügt den Eintrag hinzu
print(meinCar)
km = meinCar.setdefault("KM", 70000)  # Wenn der Wert schon existiert kann ich ihn über eine Variable herausholen
print(meinCar)
print(km)  # 50000

# dictionary.get(Key)
# Gibt den Wert zurück falls er existiert, sonst None
# print(meinCar["ABC"])  # Fehler, weil Key nicht existiert
print(meinCar.get("ABC"))  # None
print(meinCar.get("KM"))  # 50000

# dictionary.items()
# Gibt alle Key-Value Paare als Liste von Tupeln aus
print(meinCar.items())

# dictionary.keys(), dictionary.values()
# Gibt die Keys oder Values als Liste aus
print(meinCar.keys())
print(meinCar.values())

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus
list4 = list1 + list2 + list3
print(list(set(list4)))

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden
print(list("Ein Text"))

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
print(list(range(0, 21, 2)))