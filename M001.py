# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht, also muss vor jeder Zeile das # Zeichen gesetzt werden

# Wie werden Variablen definiert?
# Name = Wert
x = 5  # x angelegt als int

# Typ einer Variable ergibt sich dynamisch aus dem Wert der Variable
# In Python gibt es keine Konstanten, jede Variable kann geändert werden

# Datentypen

# Einfache Datentypen

# Integer (int)
# Ganze Zahl, egal ob positiv oder negativ
# Es gibt kein Integer Limit -> beliebig große Integer

grosseZahl = 3897453298519048659824365894365938465893456924836150239653409698  # Beliebig große Zahl möglich

# Float
# Kommazahlen, immer mit . statt mit ,
kommazahl = 324.3254

# String
# Text, wird mit "" oder mit '' angelegt
meinText = "Ein Text"
meinText2 = 'Ein Text'

# Boolean
# Wahr/Falsch Wert, True oder False möglich
wahr = True
falsch = False  # Groß geschrieben

# Stringfunktionen
# Funktionen gehören zu Objekten dazu, und haben gewisse Funktionsweisen

text = "Max Mustermann"

# string.count("")
# Gibt an, wie oft ein Text in dem angegebenen String vorkommt
# Ist Case-Sensitive
anzN = text.count("n")  # 2, Ergebnis in Variable schreiben
text.count("M")  # 2, kleines m wird nicht gefunden

# Ergebnis können wir hier nicht sehen, muss ausgegeben werden

# Exkurs: print("")
# Schreibt den angegebenen Parameter in die Konsole
print(anzN)
print(text.count("M"))

# string.lower(), string.upper()
# Gibt einen neuen String zurück, der komplett groß- oder kleingeschrieben ist
# Verändert nicht den originalen Wert
print(text.lower())
print(text.upper())
text = text.lower()  # Variable mit Ergebnis überschreiben
print(text)

# Methoden kann man verketten
print(text.lower().count("m"))

# string.islower(), string.isupper()
# Gibt einen Boolean zurück, der aussagt ob der gesamte String groß oder klein ist
print(text.islower())  # True (Zeile 58)
print(text.isupper())  # False

# Index (eckige Klammern)
# Wir können mit einem Index [] einzelne Zeichen des Strings angreifen
# Der Index beginnt bei 0 und endet bei der Länge des Strings - 1
# Benutzung: string[Index]
print(text[0])  # m
print(text[3])  # Leerzeichen

zeichen = text[0]  # Es gibt in Python keinen char Typ oder ähnliches, alles was mit Zeichen zu tun hat sind Strings
print(type(zeichen))  # type(...): gibt den Typ einer Variable aus

print(text[0].upper())  # Auch mit Strings können Verkettungen durchgeführt werden

# len(Variable)
# Gibt die Länge der Variable an
# Funktioniert nur bei Variablen mit einem Index (String, Listentypen)
print(len(text))  # 14

# print(text[len(text)])  # Versuche an Stelle 14 zu greifen -> Fehler
print(text[len(text) - 1])  # n

# Mit einem negativen Index kann man von rechts in den String greifen
print(text[-1])  # Das letzte Zeichen (n)
print(text[-4])  # m

# Range Operator
# Gibt einen Teil von einem String aus
# Fängt bei 0 an bis zum X-ten Zeichen
# Nimmt eine Stelle weniger als der normale Index (Obergrenze exkludiert)
print(text[0:5])  # max m, 01234 -> 5 ist nicht dabei
print(text[1:5])  # ax m, 1234 -> 5 ist nicht dabei
print(text[-5:-1])  # Range Operator funktioniert auch von rechts
print(text[4:])  # Bis zum Ende ohne Obergrenze
print(text[:4])  # Von 0 bis zu dem Zeichen

# string.isalpha(), string.isnumeric(), string.isalnum()
# Prüft ob ein String nur auch Buchstaben, nur aus Zahlen, oder nur aus beiden besteht
print(text.isalpha())  # False (Leerzeichen)
print(text.isnumeric())  # False
print(text.isalnum())  # False (Leerzeichen ist ein Sonderzeichen)

# complex
# Komplexe Zahlen
# j steht für den imaginären Teil
comp = 5 + 12j

# Arithmetische Operatoren in Python
# +, -, *, /
# % Modulo: Gibt den Rest einer Division zurück
# ** Potenzierung
# // Ganzzahldivision
z1 = 4
z2 = 9
print(z1 + z2)  # Es werden keine Werte verändert

z1 = z1 + z2  # Berechne das Ergebnis und schreibe es in z1 hinein
z1 += z2  # Kurzform von einer Zeile darüber

z1 %= z2
z1 **= z2
z1 //= z2  # Alle Operatoren so möglich

# Arithmetik mit Strings
text1 = "Ein"
text2 = "Test"
print(text1 + text2)  # Es werden keine Werte verändert
text1 += " " + text2
print(text1)

# Strings multiplizieren
print(text1 * 10)
text1 *= 10


# Übung1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable
z1 = 2
z2 = 4
z3 = 7
ergebnis = z1 + z2 + z3
potenz = ergebnis ** ergebnis

# Übung2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist
mod = potenz % 2

# Übung3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein
vorname = "Max"
nachname = "Mustermann"
gesamt = vorname + nachname
print(gesamt.lower().count("m"))

# Übung4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
name = 'lukas'
print(name[0].upper() + name[1:])
print(name[0].upper() + name[1:len(name)])
print(name.title())
print(name.capitalize())