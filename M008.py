import json
import csv
from os.path import exists
# Input/Output

# Es gibt in Python mehrere Funktionen für Ein-/Ausgaben
# print(...)
# input(string)
# Wartet auf den Input des Benutzers und schreibt dann die Eingabe in eine Variable
# Programm bleibt stehen bis eine Eingabe passiert

# name = input("Gib deinen Namen ein: \t")  # \t: Tabulator
# alter = input("Gib dein Alter ein: \n")  # \n: Zeilenumbruch
# print(f"Dein Name ist {name} und du bist {alter} Jahre alt")

# open(Pfad, Modus)
# Öffnet einen Stream zu einer Datei mit dem gewählten Modus
# w - Write, Overwrite
# r - Read
# a - Append
# x - Create
# r+/w+ - Read/Write, aber erstellt die Datei neu

# Funktion um ein neuen File zu erstellen anhand einen Inputs des Benutzers
# C:\Users\lk3\source\repos\Python_Grundkurs_2022_12_05
def writeInput():
	inputText = input("Gib einen Text ein: ")
	inputPfad = input("Gib einen Pfad ein: ")
	if not exists(inputPfad):  # exists: Funktion in os.path, mit Alt + Eingabe importieren
		file = open(inputPfad, "w+")  # File öffnen und erstellen wenn es nicht existiert
		file.write(inputText)  # Text schreiben
		file.close()  # File schließen (wichtig)
	else:
		print("File existiert bereits")

# writeInput()

if exists("Test.txt"):
	readFile = open("Test.txt", "r")
	lines = readFile.readlines()  # Alles einlesen
	for line in lines:
		print(line)
	readFile.close()

# with-Block: wird automatisch geschlossen, wenn der Block zu Ende ist
with open("Test.txt", "r") as readFile:
	lines = readFile.readlines()
	for line in lines:
		print(line)
# hier wird der with Block geschlossen

# rstring
# Raw string
# Interpretiert alles als string (Escape Sequenzen, Backslash, ...)
rstring = r"\n\t\\"
print(rstring)

# Besonders nützlich für Pfade
pfad = r"C:\Users\lk3\source\repos\Python_Grundkurs_2022_12_05"

# Json
numList = [1, 2, 3, 4, 5]
with open("Test2.txt", "w+") as writeFile:
	json.dump(numList, writeFile)

with open("Test2.txt", "r+") as readFile:
	print(json.load(readFile))

jsonString = json.dumps(numList)
print(jsonString)

numListConvert = json.loads(jsonString)
print(numListConvert)

# Übung:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden