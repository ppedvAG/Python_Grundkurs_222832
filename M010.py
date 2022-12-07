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
