import sys
import numpy
import math

from M007 import countCase

countCase("Das ist ein Text")

# Module-Searchpath
# 1. Im selben Ordner, wie das ausgeführte Skript
# 2. PYTHONPATH, Ordner in dem Python selbst installiert ist
# 3. Liste an Ordnern, die wir bei der Installation von Python zusätzlich konfiguriert haben
# Wenn nach Punkt3 nichts gefunden wird => ModuleNotFoundError

# sys Modul
# Alle möglichen Informationen zur Umgebung
# z.B.: Version, Suchpfade für Module, ...
print(sys.version)
print(sys.path)
# sys.exit(0) # sys.exit(Code): Programm beenden, 0: alles OK, 1: Fehler

def main():
	print("Ich führe M007b aus")
	countCase("Test")
	numpy.floor(4.4)
	math.floor(4.4)


# Wie installiere ich ein zusätzliches Modul?
# 1. Entweder per Terminal:
# pip install <Name>
# pip uninstall <Name>
# 2. Über Python Packages Tab in PyCharm unten links

if __name__ == "__main__":
	main()