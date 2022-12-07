# Unittesting

# Teile meines Programms auf Fehler testen
# Erwartetes Verhalten im Test festlegen und dann den laufen lassen
# Schauen was passiert, über Konsolenausgabe sehen wir ob der Test erfolgreich war oder nicht

import unittest
from unittest import TestCase
from M013b import Rechner

class TestClass(TestCase):
	def testeAddiere(self):
		# Arrange (Rahmenbedingungen festlegen)
		r = Rechner()
		expected = 7
		x, y = 3, 4

		# Act (Code den ich testen möchte ausführen)
		result = r.add(x, y)

		# Assert (Testresultat begutachten)
		self.assertEqual(result, expected)

	def testeSubtrahiere(self):
		r = Rechner()
		expected = -5
		x, y = 4, 9

		result = r.sub(x, y)

		self.assertEqual(result, expected)

class TestClass2(TestCase):
	def testeMultiplizieren(self):
		# Arrange (Rahmenbedingungen festlegen)
		r = Rechner()
		expected = 12
		x, y = 3, 4

		# Act (Code den ich testen möchte ausführen)
		result = r.mult(x, y)

		# Assert (Testresultat begutachten)
		self.assertEqual(result, expected)

	def testeDividiere(self):
		# Arrange (Rahmenbedingungen festlegen)
		r = Rechner()
		expected = 1.5
		x, y = 6, 4

		# Act (Code den ich testen möchte ausführen)
		result = r.div(x, y)

		# Assert (Testresultat begutachten)
		self.assertEqual(result, expected)

if __name__ == '__main__':  # Muss existieren um Tests zu aktivieren
	unittest.main()