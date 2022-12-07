# from M006 import countCase

# Fehlerbehandlung

def doStuff(test):
	print(test)

# doStuff()  # Zu wenige Parameter (Syntax Error in PyCharm), TypeError zur Laufzeit

def rec():
	rec()

# rec()  # RecursionError, da sich die Funktion selbst aufruft

# zahl = int(input("Gib eine Zahl ein: "))  # ValueError, wenn der User keine Zahl eingibt

# countCase([1, 2, 3])  # AttributeError

try:  # Hier kommt der Code der Fehler verursachen könnte
	zahl = int(input("Gib eine Zahl ein: "))  # Hier könnte ein ValueError (keine Zahl) oder EOFError (Strg + D) passieren
	print(5 / zahl)  # Hier kann ein ZeroDivisionError auftreten wenn der User keine Zahl eingibt
except ValueError as e:
	# Hier werden einzelne Fehler abgefangen
	# as e: Um den Error auszugeben (in ein Log z.B.)
	print(e)
	print("Keine Zahl")
except EOFError as e:  # Hier e nochmal möglich, e ist nur im entsprechenden except Block sichtbar
	# Strg + D abfangen
	print(e)
	print("Strg + D ist nicht erlaubt")
except ZeroDivisionError as e:
	# Division durch 0 abfangen
	print("Division durch 0 nicht möglich")
except Exception as e:
	# Alle anderen Errors fangen
	# Dieser Code wird nicht ausgeführt wenn ein anderer Fehler gefangen wird
	print("Anderer Fehler")
except:
	# Alle anderen Errors fangen
	# Selber Effekt wir Block darüber
	print("Anderer Fehler")
else:
	# Wird ausgeführt, wenn der try Block fehlerfrei ausgeführt wird
	print("Alles fehlerfrei ausgeführt")
finally:
	# Finally Block wird immer ausgeführt, auch wenn ein Fehler aufgetreten ist
	print("Alles fertig")

print("Nach dem try-except")

# Raise
# Eigenen Fehler werfen + Fehlermeldung
# Kann auch eigens erstellte Fehler werfen
# raise ValueError("Der Wert ist nicht valide")

# Eigenen Error definieren
class CoffeeError(Exception):
	status = ""

	def printStatus(self):
		print(self.status)

	def __init__(self, message, status):
		super().__init__(message)  # Message an die Exception Klasse übergeben
		self.status = status

# Eigenen Error werfen
# raise CoffeeError("Wir haben keinen Kaffee mehr!")

try:
	coffee = 0
	if coffee < 1:
		raise CoffeeError("Wir haben keinen Kaffee mehr!", "Kaffee=0")  # Eigenen Fehler werfen
	elif coffee <= 5:
		raise ValueError("Es ist nurnoch wenig Kaffee da")  # Pythoninternen Fehler werfen
	else:
		print("Kaffee ist noch da")
except CoffeeError as e:
	print(e)  # Wir haben keinen Kaffee mehr!
	print("Jemand muss Kaffee kaufen")
	e.printStatus()  # Im except habe ich ein CoffeeError Objekt