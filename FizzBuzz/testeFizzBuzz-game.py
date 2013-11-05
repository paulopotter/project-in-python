import unittest
from testado import *
testado = FizzBuzz()
i = 15

class TestFizzBuzz(unittest.TestCase):
	def testFizz(self):
		self.assertEqual(testado.fizz(i),'Fizz')
	def testBuzz(self):
		self.assertEqual(testado.buzz(i),'Buzz')
	def testFizzBuz(self):
		self.assertEqual(testado.fizzBuzz(i),'FizzBuzz')
	def testJogoFizzBuzz(self):
		self.assertEqual(testado.jogoFizzBuzz(i),'FizzBuzz')




# executando o teste
if __name__ == '__main__':
	unittest.main()