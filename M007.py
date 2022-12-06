# Module in Python
# Sind Bibliotheken, die uns zusätzliche Funktionalität anbieten die wir einbinden können
# Enhalten nur Code der sich mit einem Thema befasst
# Müssen importiert oder installiert werden

# Wie importiere ich ein Modul?
# Syntax:
# import <Modulname>
# from <Modulname> import <Funktion(en)> (as <Alias>)

# import turtle  # Holt turtle.py, bindet Funktionen nicht direkt ein
# from turtle import *  # Bindet Funktionen direkt in unseren Code ein

# speed(10)
# color('red', 'blue')
# begin_fill()
# while True:
#     forward(300)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# Die Variable __name__ enthält den Namen der Python Datei
# Falls die Datei direkt ausgeführt wurde, ist der Name immer __main__
# Falls die Datei importiert wird ist __name__ der tatsächliche Dateiname (M007 hier)
print(__name__)

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

if __name__ == "__main__":  # Wenn das Skript direkt ausgeführt wird
	# exit()  # Beendet das Programm, wenn das Skript direkt gestartet wird
	print("Test")
	print("Ich bin das Hauptskript")
	print(__name__)