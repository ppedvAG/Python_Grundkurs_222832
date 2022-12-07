# Lambda Expressions

# Lambdas sind anonyme Funktionen, also Funktionen die in einer Variable gespeichert werden können
# In anderen Sprachen mit =>, ->
# In Python gibt es das Lambda Keyword
# Eigenschaften
# - Kein Name
# - Beliebig viele Parameter
# - Optionaler return Wert, falls ein return Wert braucht die Funktion kein return
# - Darf nur eine Expression enthalten
# - Keine Schleifen und kein break/continue

# Syntax
# lambda <Par1>, <Par2>, ... : <Code>
add = lambda z1, z2: z1 + z2  # return integriert
print(add(4, 5))

printAdd = lambda z1, z2: print(z1 + z2)
printAdd(6, 3)

def addF(z1: int, z2: int) -> int:  # Äquivalent zur add Lambda-Expression
	return z1 + z2

printZahlen = lambda *zahlen: print(sum(zahlen))  # Auch * und ** Argumente sind möglich
printZahlen(*[1, 2, 3, 4, 5])


def test(exp):  # Lambda-Expression als Parameter
	print(exp(5, 6))

test(add)  # Lambda-Methodenzeiger übergeben
test(addF)  # Methodenzeiger von einer definierten Funktion übergeben
test(lambda z1, z2: z1 - z2)  # Lambda direkt übergeben

# Lambdas werden häufig als Parameter für Methoden verwendet
# filter(): filtert eine Liste
# map(): wandelt eine Liste in eine andere Form um

# Die filter() Funktion
# Syntax:
# filter(Funktion, Liste)
# Filtert die Liste anhand der angegebenen Funktion
# Die Funktion muss bool zurückgeben
numberList = list(range(100))

# numberList nach Zahlen die durch 3 teilbar sind filtern
# Liste filtern mit for
div3List = []
for i in numberList:
	if i % 3 == 0:
		div3List.append(i)
print(div3List)

# Liste filtern mit Lambda
div3ListLambda = list(filter(lambda numL: numL % 3 == 0, numberList))  # ohne list(...) gibt filter nur ein filter Object zurück
print(div3ListLambda)

# Liste filtern mit List-Comprehension
div3ListLC = [num for num in numberList if num % 3 == 0]
print(div3ListLC)

# Ich kann statt Lambda auch eine seperate Funktion definieren
def mod3(num: int):
	return num % 3 == 0

print(list(filter(mod3, numberList)))  # Hier einfach Methodenzeiger auf richtige Methode übergeben

# Die map() Funktion
# Syntax:
# map(Funktion, Liste)
# Wandelt die Liste in eine neue Form um
# Die Funktion darf keinen Wert zurückgeben

numberListMap = list(range(100))

# Alle Zahlen mit 4 multiplizieren
for i in range(len(numberListMap)):
	numberListMap[i] *= 4
print(numberListMap)

# Mit map
numberListMap = list(range(100))
mal4Map = list(map(lambda num: num * 4, numberListMap))
print(mal4Map)

# Wir wollen die Liste zu einer String Liste umwandeln
# for
for i in range(len(numberListMap)):
	numberListMap[i] = f"Die Zahl ist {numberListMap[i]}"
print(numberListMap)

# map
numberListMap = list(range(100))
stringMap = list(map(lambda num: f"Die Zahl ist {num}", numberListMap))
print(stringMap)

# Extra Spalte
spaltenList = list(range(10))
spaltenList = list(map(lambda num: (num, num ** num), spaltenList))
print(spaltenList)

spaltenList = list(range(10))
for i in range(len(spaltenList)):
	z = spaltenList[i]
	spaltenList[i] = (z, z ** z)
print(spaltenList)