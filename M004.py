# Schleifen
# Wenn man etwas mehrmals hintereinander machen möchte

# While Schleife
# Läuft solange die Bedingung True ist
# Zähler sollte dabei sein (in den meisten Fällen)
i = 0
while i < 10:  # Bedingung, Schleife läuft bis die Bedingung false ist
	print(i)
	i += 1  # Wichtig: Zähler erhöhen
else:  # Wird nach der Schleife ausgeführt, wenn die Schleife fehlerfrei ausgeführt wurde (ohne break)
	print("Schleife fertig")

while True:
	print("Text")
	i += 1
	if i == 500:
		break  # Beende die Schleife, sollte immer mit einer if/elif/else kombiniert werden
else:  # Wird nie ausgeführt
	print("Schleife fertig")

# for Schleife
# Verhält sich wie foreach in anderen Sprachen
# Wird verwendet um über eine Collection zu iterieren (List, Tuple, String, Range, ...)
# Syntax:
# for <Variablenname> in <Liste>:
liste = ["Ich", "bin", "eine", "Liste"]

for wort in liste:  # wort: Variablenname für das derzeitige Wort
	print(wort)
	print("Ein Wort wurde geschrieben")  # Mehrere Codezeilen in einer Schleife ausführen

# for Schleife mit Zähler
for i in range(0, 10):  # Eine Schleife die von 0 bis 9 geht
	print(i)

text = "Ein Text"
for zeichen in text:  # Mit for-Schleife über String gehen
	print(zeichen)

# break und continue
# break: Die Schleife beenden und mit dem Code danach weitermachen
# continue: Zum Schleifenkopf zurückspringen und den Code danach nicht ausführen
for i in range(0, 10):
	print(i)
	if i == 5:
		break  # Wenn i == 5, beende die Schleife

print("Test")

for i in range(0, 10):
	if i == 5:
		continue  # Wenn i == 5, gehe zum Schleifenzurück und überspringe den Code danach
	print(i)

# else am Ende einer Schleife
# Geht auch bei for
for i in range(0, 10):
	print(i)
else:
	print("Schleife fertig")

# fstring
# Code in einen String schreiben
# Syntax:
# f"Text1 Text2 {<Code>}"
a = 5
str2 = "Text1 Text2 " + a.__str__()  # ohne fstring
fstring = f"Text1 Text2 {a}"  # einfach a einbinden und wird automatisch konvertiert
print(fstring)

# Ich möchte pro Schleifendurchlauf immer i, i^2 und die Gleichung ausgeben
for i in range(0, 10):
	# Ohne fstring
	print("Die Zahl ist " + i.__str__())
	print("Die Quadrierte Zahl ist " + (i*i).__str__())
	print(i.__str__() + "^2=" + (i*i).__str__())

	# Mit fstring
	print(f"Die Zahl ist {i}")
	print(f"Die Quadrierte Zahl ist {i*i}")
	print(f"{i}^2={i*i}")

# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden