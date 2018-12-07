import unittest

class BaseTestClass(unittest.TestCase):

	def test_add(self):
		self.assertEquals(120, 100 + 20)
		self.assertFalse(10 > 20)
		self.assertGreater(120, 100)

	def test_sub(self):
		self.assertEquals(100, 140 - 40)

if __name__ == '__main__':
	unittest.main()
