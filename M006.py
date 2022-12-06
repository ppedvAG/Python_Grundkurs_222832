# Funktionen

# Ein Code Block der nur ausgeführt wird wenn wir ihn aufgerufen
# Beispiele: len(...), list(...), upper(), ...
# print(...)

# Wir können auch eigene Funktionen definieren
# Funktionen für wiederverwendbarkeit
# Syntax:
# def <Name>(<Parameter1>, <Parameter2>, ...):
# 	Code
# <Name>(<Par1>, <Par2>, ...)


def hallo():  # Funktion angelegt ohne Parameter
	print("Hallo")

hallo()  # Funktion aufrufen
hallo()


def halloName(name):  # Funktion mit Parameter
	print(f"Hallo {name}")

halloName("Lukas")
halloName(123)
halloName(True)
halloName({1, 2, 3})  # Alle möglichen Parameter möglich

length = len("Hallo Welt")  # 10 als Rückgabewert
print(length)  # Den Rückgabewert verwenden


def addiere(x, y):
	return x + y  # Ergebnis zurückgeben

ergebnis = addiere(5, 4)  # Ergebnis aus der Funktion in eine Variable schreiben
print(ergebnis)


def addiereFix(x: int, y: int):  # mit :<Typ> bei einzelnen Parametern einen Typ empfehlen
	return x + y

print(addiereFix(5, 4))
print(addiereFix([1, 2, 3], [1, 2, 3]))  # Diese Eingabe funktioniert trotz Empfehlung
print(addiereFix(5.5, 2.2))  # Auch mit Floats funktioniert die Funktion

def addiereFixerReturn(x: int, y: int) -> float:  # mit -> <Typ> den Rückgabetyp angeben
	return x / y

kommazahl = addiereFixerReturn(5, 3)
print(kommazahl)

# Default Werte
# Bei einem Parameter angeben was der Standardwert ist, und muss dann beim Aufruf diesen nicht übergeben
def subtrahiere(x: int, y: int, yMinusX=False):
	if yMinusX:
		return y - x
	else:
		return x - y

print(subtrahiere(8, 4))  # yMinusX weggelassen
print(subtrahiere(8, 4, True))  # yMinusX explizit setzen

# Die Reihenfolge von Parametern kann verändert werden
print(subtrahiere(y=3, x=10, yMinusX=True))

# Hier eine Funktion mit sehr viele Parametern
def generierePerson(vn="", nn="", alter=0, adresse="", geschlecht=""):
	print()

generierePerson(alter=30, adresse="Zuhause")  # Bestimmte Parameter weglassen

# Arbitrary Arguments
# * Parameter
# Gibt die Möglichkeit beliebig viele Parameter zu übergeben
# Syntax: *name


def sumNumbers(*numbers: int):  # Tuple mit allen Parameter
	x = 0
	for num in numbers:
		x += num
	return x

print(sumNumbers(1, 2, 3, 4, 5, 6, 7.8))  # beliebig viele Parameter
print(sumNumbers())  # Auch keine Parameter sind beliebig viele Parameter

# Unpacking Operator
# Teilt die Liste auf ihre einzelnen Bestandteile auf
nummern = [1, 2, 3, 4, 5]
# sumNumbers(nummern)  # Funktioniert nicht
print(sumNumbers(*nummern))  # Hier wird die Liste in ihre Einzelteile zerlegt
print(sumNumbers(*range(1, 100)))  # Besonders Praktisch bei Range


def buchstabiere(*wort):
	for zeichen in wort:
		print(zeichen)

buchstabiere("text")  # Dieser Text wird in der Funktion oben als Tupel interpretiert
buchstabiere(*"text")  # Dieser Text wird aufgeteilt

# (a, b, c, d) = (1, 2, 3, 4, 5, 6)  # Nicht möglich, da zu viele Werte
(a, b, *c, d) = (1, 2, 3, 4, 5, 6)  # Eine Variable mit * versehen, damit alle Werte die zu viel sind in diese Variable gefüllt werden
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]
print(d)  # 6

# Arbitrary Keyword Arguments
# Ermöglicht uns bei einer Funktion ein Dictionary zu übergeben

testDict = {
	"Name1": "Wert1",
	"Name2": "Wert2",
	"Name3": "Wert3"
}

def halloGuests(**guests):
	for key, value in guests.items():  # Dictionary in Python durchgehen, gleichzeitig auf Key und Value zugreifen
		print(f"{key}: {value}")

halloGuests(**testDict)  # Hier auch wieder Unpacken

def multiply(z1, z2, /, z3, z4):
	return z1 * z2 * z3 * z4

# multiply(z3=5, z1=3, z2=5, z4=7)  # Mit / als Parameter müssen die Parameter davor in der richtigen Reihenfolge angegeben werden
multiply(3, 5, z4=7, z3=8)

def passTest():
	pass  # Mach garnix

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
def Max(*numbers):
	m = 0  # numbers[0] um auch negative Zahlen zu berücksichtigen
	for i in numbers:
		if i > m:
			m = i
	return m

def Maximum(*numbers):
	return max(numbers)

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Bonus: Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12

def countCase(text: str):
	lower, upper, special = 0, 0, 0
	for char in text:
		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		else:
			special += 1
	print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")

countCase("Ein Text")

text = "5"
if text.upper() == text.lower():  # Sonderzeichen überprüfen
	print("Sonderzeichen")