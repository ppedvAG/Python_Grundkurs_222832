# Vererbung
# Klassen können eine Oberklasse haben und damit einer Hierarchie herstellen
# z.B.: Lebewesen -> Mensch, Hund, Katze
# Lebewesen ist die Oberklasse von Mensch, Hund und Katze und gibt ihre Variablen und Funktionen nach unten weiter
# Lebewesen hat name: str, bewegen(distanz: int)
# Unterklassen haben die Variable und die Funktion dann auch

class Lebewesen:
	name = ""

	def bewegen(self, distanz: int):
		print(f"Das Lebewesen hat sich {distanz}m bewegt")

	# __init__ wird auch weiter vererbt
	def __init__(self, name: str):
		self.name = name
		print(f"Ein {type(self).__name__} wurde erstellt")  # type(self) ist Vererbungsunabhängig -> es kommt der Typ des derzeitigen Objekts heraus, __name__ um nur den Namen zu holen statt <class '__main__.Mensch'>

	# __str__ wird auch weiter vererbt
	def __str__(self):
		return f"Mein Name ist {self.name}"

# Mensch ist ein Lebewesen
# Für Vererbung muss die Oberklasse in der Klammer stehen
# Mensch erbt name und bewegen(int) von Lebewesen
class Mensch(Lebewesen):
	alter = 0
	"""
	Variablen können auch beschrieben werden
	"""

	# Überschreibe die Implementation in Lebewesen
	def __init__(self, name: str, alter: int):
		super().__init__(name)  # mit super() auf Funktionen/Variablen der Oberklasse zugreifen
		self.alter = alter  # Alter setzen

	# An die obere Methode weitere Strings anhängen
	def __str__(self):
		lw = super().__str__()
		return f"{lw} und mein Alter ist {self.alter}"

	def sprechen(self):
		print("Der Mensch redet")

class Katze(Lebewesen):
	pass

mensch = Mensch("Lukas", 24)
mensch.bewegen(10)  # Funktion wurde vererbt
print(mensch)  # __str__ in Mensch wird verwendet
print(mensch.sprechen())

lw = Lebewesen("Name")
# lw.sprechen() # Funktionen werden nicht nach oben weitergegeben

# Übung:
# Erstelle eine Klasse Fahrzeug
# Sie soll über die folgenden Properties verfügen:
# Motorstatus: bool -> Gibt an ob der Motor gestartet ist oder nicht
# maximale Geschwindigkeit: int
# derzeitige Geschwindigkeit: int
# Sie soll die __init__ Methode implementieren mit den obigen Parametern
# Sie soll die __str__ Methode implementieren
# Sie soll eine beschleunigung Methode implementieren, diese akzeptiert einen Parameter, die neue Geschwindigkeit
# Wenn die neue Geschwindigkeit <= maximale Geschwindigkeit ist und der Motor gestartet ist, soll die derzeitige Geschwindigkeit angepasst werden

class Fahrzeug:
	"""
	Die Fahrzeug Klasse aus der Übung. Sie kann beschleunigen.
	"""
	def __init__(self, motorstatus: bool, maxV: int, aktV: int):
		"""
		Hier werden die Standardwerte gesetzt, Motorstatus muss True sein damit die aktV gesetzt wird (sonst ist aktV 0).

		:param motorstatus: Ob der Motor läuft oder nicht (bool)
		:param maxV: Die maximale Geschwindigkeit (int)
		:param aktV: Die aktuelle Geschwindigkeit (int)
		"""
		self.motorstatus = motorstatus
		self.maxV = maxV
		if motorstatus:
			self.aktV = aktV
		else:
			self.aktV = 0


	def __str__(self):
		"""
		Gibt das Objekt schön formatiert zurück.

		:return: Das Objekt formatiert als String.
		"""
		return f"Das Fahrzeug hat eine Maximalgeschwindigkeit von {self.maxV}, es fährt gerade ({self.motorstatus}) und fährt {self.aktV}km/h."


	def beschleunige(self, v: int):
		"""
		Beschleunigt das Fahrzeug um die angegebene Geschwindikeit (v). V kann auch negativ sein.
		Das Fahrzeug kann nicht über die Maximalgeschwindigkeit beschleunigen und nicht unter 0km/h bremsen.

		:param v: Die Geschwindigkeit die aufaddiert werden soll.
		"""
		if self.motorstatus:
			if self.aktV + v > self.maxV:
				print("Zu hoch")
			elif self.aktV + v < 0:
				print("Zu niedrig")
			else:
				self.aktV += v
		else:
			print("Motor nicht gestartet")

fzg = Fahrzeug(True, 300, 0)
fzg.beschleunige(200)
print(fzg)

# docstring
# Um Code zu beschreiben
# Wird unter Klassen-/Variablen- und Funktionsdefinitionen geschrieben
# Wird mit """ geöffnet und mit """ geschlossen
# In großen Projekten sehr relevant, damit jedem Mitarbeiter bekannt ist was der Code tut