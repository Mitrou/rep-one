import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	@staticmethod
	def test_loading_time():
		assert requests.get("http://www.python.org").elapsed.total_seconds() < 0.8

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
