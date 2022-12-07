import time

# Decorator
# Funktion, die auf eine andere Funktion angehängt werden kann
# Werden mit @<Name> hinzugefügt

# Auch Funktionen sind Objekte
def test():
	pass

print(test)  # Function Objekt

testFunc = test  # Funktion kann auch auf Variablen gehängt werden
print(testFunc)

def testDecorator(func):  # func: Funktion die mit dem Decorator versehen wird
	def wrapper():  # Code der vor oder nach der Funktion ausgeführt wird
		print("Vor der Funktion")
		func()
		print("Nach der Funktion")
	return wrapper  # Hier kommt der fertige Decorator heraus (ohne Klammern)

def hello():
	print("Hello World")

decoratedHello = testDecorator(hello)  # Hier lasse ich hello dekorieren
decoratedHello()  # Vor/nach der Funktion werden jetzt ausgeführt

# Kurzform:

@testDecorator
def bye():
	print("Bye World")

bye()

# Decorator mit Parameter
def doTwice(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper

@doTwice
def printAddiere(z1, z2):
	print(z1 + z2)

printAddiere(4, 5)

# Decorator mit Return Wert
def doTwiceReturn(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
	return wrapper

@doTwiceReturn
def add(z1, z2):
	print(f"{z1}+{z2}={z1 + z2}")
	return z1 + z2

print(add(7, 8))

# Decorator zum Messen der Ausführungszeit
def measureTime(func):
	def wrapper(*args, **kwargs):
		startTime = time.time()
		func(*args, **kwargs)
		endTime = time.time()
		print(f"{endTime - startTime}s vergangen")
	return wrapper

@measureTime
def sumNumbers(*args):
	return sum(args)

sumNumbers(*range(100000000))

class Square:
	def __init__(self, a):
		self._seitenlaenge = a  # interne Variable

	@property
	def seitenlaenge(self):
		print("Die Seitenlänge wurde angegriffen")
		return self._seitenlaenge

	@seitenlaenge.setter
	def seitenlaenge(self, neuerWert):
		if neuerWert > 0 and neuerWert < 100:
			self._seitenlaenge = neuerWert
		else:
			print("Neue Seitenlänge nicht gültig")

square = Square(20)
print(square.seitenlaenge)  # property
print(square._seitenlaenge)  # Geht trotzdem, da private auch nur eine Empfehlung
square.seitenlaenge = 300  # Normalerweise können Funktionen nicht gesetzt werden, aber durch Setter ist das möglich