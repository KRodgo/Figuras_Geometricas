import unittest
#
from area import area

class areaTest(unittest.TestCase):
	def setUp(self):
		self.calc=area()

	def test_cuadrado(self):
		self.assertEquals(self.calc.area(1,5,0,0),25)

	def test_rectangulo(self):
		self.assertEquals(self.calc.area(2,2,6,0),12)

	def test_circulo(self):
		self.assertEquals(self.calc.area(3,2,0,0),12.5664)

	def test_Trapecio(self):
		self.assertEquals(self.calc.area(4,8,4,8),48)

if __name__ == '__main__':
	unittest.main()
 	