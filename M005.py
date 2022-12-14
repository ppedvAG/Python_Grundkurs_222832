# List Comprehension
# Anhand eines Ausdrucks kann man eine Liste konstruieren
numbers = [number for number in range(0, 101)]  # Alle Ergebnisse der for-Schleife werden in die Liste geschrieben
print(numbers)

evenNumbers = [num for num in range(0, 101) if num % 2 == 0]  # if noch hinzufügen
print(evenNumbers)

print([num ** num for num in range(1, 11)])  # Zahl vor dem Einfügen in die Liste noch bearbeiten

print([num ** num for num in range(1, 20) if num ** num % 2 == 0])  # Nur gerade Zahlen beim Potenzieren einfügen

# Ohne List-Comprehension
# testList = []
# for num in range(1, 20):
# 	if num ** num % 2 == 0:
# 		testList.append(num ** num)
# print(testList)

# Verschachtelte Schleifen in List Comprehension
print([f"{z1}x{z2}={z1*z2}" for z1 in range(1, 11) for z2 in range(1, 11)])  # Kleines 1x1 mit List Comprehension

print([f"{num} gerade" if num % 2 == 0 else f"{num} ungerade" for num in range(0, 101)])  # Ternary Operator hier sehr nützlich

# List Comprehension mit String Liste
stringListe = ["IcH", "bIN", "eiN", "TeXt", "Ein"]

print([wort.upper() for wort in stringListe])  # Ganze Liste groß schreiben

print([wort.upper() if wort[0].isupper() else wort.lower() for wort in stringListe])  # Alle Wörter die einen großen Anfangsbuchstaben haben werden groß geschrieben, alle anderen Wörter klein

print([wort.title() if wort[0].isupper() else wort.lower() for wort in stringListe])  # Liste Fehler beheben

print([wort for wort in stringListe if "e" in wort])  # Alle Wörter mit e finden

print([wort for wort in stringListe if "e" in wort.lower()])  # Alle Wörter mit e finden (Case-Insensitive)

umlaut = ["Wörter", "Für", "Änderung", "Wort"]
print([wort.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").title() for wort in umlaut])  # Umlaute ersetzen

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden
print([num + 12 for num in range(1, 31) if num % 6 == 0])

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
text = "Ich bin ein Text"
print([b.upper() for b in text if b.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
print([wort[0] for wort in text.split(" ")])
print([wort[0] for wort in text.title() if wort.isupper()])

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
print([wort for wort in text.split(" ") if len(wort) <= 3])

# Match-Case (switch)
# if/elif/else Konstrukte vereinfachen

# Syntax:
# match <Variable>
# 	case <Bedingung>:
# 		Code
# 	case <Bedingung>:
# 		Code

text = "Test"
if text == "Ein Text":
	print()
elif text == "Zwei Text":
	print()
elif len(text) >= 5:
	print()
else:
	print()

match text:
	case "Ein Text":
		print()
	case "Zwei Text":
		print()
	case _ if len(text) >= 5:  # _ if um andere Bedingungen als == zu benutzen
		print()
	case _:  # default case
		print()