# Kontrollstrukturen

# Werden in Kombination mit logischen Operatoren verwendet

# Vergleichsoperatoren
# <, >, <=, >= kleiner, größer, kleiner-gleich, größer-gleich | Ergebnis True oder False
# ==, != gleich, ungleich

# if-Anweisung
# Überprüft eine Bedingung und führt den Code darin nur aus wenn diese Bedingung wahr ist
a = 4
b = 8

if a < b:  # Code unterhalb wird nur ausgeführt wenn die Bedingung True ist
	print("A kleiner B")  # Durch Tabs die Ebenen festlegen
	print("If Ende")  # Mehrere Teile Code in der selben If

print("Nach der If")  # Nach der If ohne Einrückung

# elif
# Wird ausgeführt wenn die if nicht True ist und hat eine zusätzliche Bedingung
if a < b:
	print("A kleiner B")
elif a > b:  # wird nicht ausgeführt wenn die if ausgeführt wird
	print("A größer B")

# else
# Wird ausgeführt, wenn keine if/elif ausgeführt wird
# Wenn irgendwas anderen passiert
if a < b:
	print("A kleiner B")
elif a > b:
	print("A größer B")
else:
	print("A gleich B")

# Bei mehreren if-Statements hintereinander wird jedes geprüft
c = 100
if c > 100:
	print("c größer 100")
if c > 90:
	print("c größer 90")
if c > 80:  # Beide ifs werden betreten, da sie nicht mit elif zusammenhängen
	print("c größer 80")
else:  # Dieses else hängt nur mit der letzten if zusammen
	print("c kleiner-gleich 80")

if c > 100:
	print("c größer 100")
elif c > 90:
	print("c größer 90")
elif c > 80:  # Dieses elif wird nicht betreten
	print("c größer 80")
else:  # Dieses else hängt nur mit der letzten elif zusammen
	print("c kleiner-gleich 80")

# elif wird nur betreten wenn die vorherige if/else False war

if a < b:
	print("a ist kleiner als b")
	if a % 2 == 0:  # Wenn a gerade ist
		print("a ist gerade")  # Der Codeblock muss nochmal eingerückt werden
	else:  # Anhand Einrückungen kann die else bei der inneren if oder der äußeren if angehängt werden
		print("a ist ungerade")

# Logische Operatoren
# and: Zwei Bedingungen verknüpfen, ist nur True wenn beide Bedingungen True sind
# or: Zwei Bedingungen verknüpfen, ist True wenn eine der Bedingungen True ist oder beide
# not: Bedingung invertieren
# in: Ist ein Element in einer Liste enthalten?
# is: Sind Zwei Objekte identisch, schaut auf Speicheradressen

d = 10
if a < b and a > c or not b == c:  # Mehrere Bedingungen mit and/or verbinden
	print("a ist kleiner als b und a ist größer als c und b ist nicht gleich c")

liste = [1, 2, 3, 4]
if 3 in liste:
	print("3 ist in der Liste enthalten")
else:
	print("Liste enthält keine 3")

# Ternary Operator
# Ermöglicht Verkürzung von If/Elses

if a < b:
	print("a kleiner b")
else:
	print("a größer-gleich b")

print("a kleiner b") if a < b else print("a größer-gleich b")  # Mit Ternary
print("a kleiner b" if a < b else "a größer-gleich b")  # Mit Ternary

if a < b:
	print("A kleiner B")
elif a > b:
	print("A größer B")
else:
	print("A gleich B")

print("A kleiner B") if a < b else print("A größer B") if a > b else print("A gleich B")  # Mit Ternary

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)
if len(list1) > len(list2) and len(list1) > len(list3):
	print("list1 > list2 & list3")
elif len(list2) > len(list1) and len(list2) > len(list3):
	print("list2 > list1 & list3")
else:
	print("list3 > list1 & list2")

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
newList = list1 + list2 + list3
if 3 in newList or 7 in newList or 10 in newList:
	print("3, 7, oder 10 ist enthalten")