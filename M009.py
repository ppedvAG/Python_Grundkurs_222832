# Klassen und Objekte

# Objekte
# Alles in Python ist ein Objekt
# Jedes Objekt hat einen Typen (int, str, list, ...)
# Jedes Objekt hat die Variablen und Funktionen die von der Klasse vorgegeben werden

i = 12  # Variable mit 12 (int) Objekt
i.as_integer_ratio()  # Variable hat die Funktion aus der Klasse
print(type(i))  # <class 'int'>

# isinstance
# Überprüft ob eine Variable ein bestimmter Typ ist
print(isinstance(i, int))  # True
print(isinstance(i, str))  # False
print(isinstance(i, object))  # True

# Klasse
# Eine Klasse ist ein Bauplan, aus dem Objekte erstellt werden können
# In der Klasse wird vorgegeben, wie das Objekt aussieht -> Funktionen und Variablen definieren

# Wie erstelle ich eine Klasse?
# Mit dem class Keyword und mit einem Namen

class Person:
	name = ""  # Klassenattribut

	# Funktion definieren, alle Objekte des Typs Person haben dann diese Methode
	# self: Das Objekt selbst, am Anfang jeder Funktion
	def speak(self, text: str):
		print(f"Mein Name ist {self.name}, {text}")

	# Konstruktor
	# __init__: Code der ausgeführt wird, wenn das Objekt erstellt wird
	def __init__(self, alter=0):  # Werte für die Erstellung des Objekts angeben
		print("Das Objekt wurde erstellt")
		self.alter = alter  # Variablen festlegen -> werden zu Klassenvariablen

	# __str__: Gibt eine Repräsentation des Objekts als string zurück
	# Wird aufgerufen, wenn das Objekt selbst geprinted wird
	def __str__(self):
		return f"Mein Name ist {self.name} und mein Alter ist {self.alter}."

# Wie erstelle ich ein Objekt?
# <Klassenname>()
person = Person(20)  # Alter hier übergeben
print(person.name)  # Variable kommt von der Klasse
person.name = "Lukas"
print(person.name)
person.speak("Ich bin eine Person")  # Funktion kommt von Klasse
print(person.alter)  # Variable aus __init__ hier sichtbar

# Verwendet __str__
# Wenn __str__ nicht definiert ist -> <__main__.Person object at 0x0000025FA9F1BFD0>
# Modul.Typ, Speicheradresse
print(person)

# In Python können Objekte neue Attribute erhalten
# <Variablenname>.<Neuer Name> = <Wert>
# Dynamische Variablen sollten vermieden werden
person.adresse = "Teststraße 1"
print(person.adresse)

del person.adresse  # del: Variable/Funktion löschen

print(type(person))  # __main__.Person
print(isinstance(person, Person))  # True
print(isinstance(person, object))  # True