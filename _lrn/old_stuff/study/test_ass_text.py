__author__ = 'SM'
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import re

class BaseFlow(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def test_1page_open(self):
		browser = self.browser
		browser.get("http://b2lead:Mk18mod0@stg.b2lead.com")
		self.assertIn("B2L San Diego", browser.title)

	def test_2allbaseflow(self):
		browser = self.browser
		browser.get("http://b2lead:Mk18mod0@stg.b2lead.com")
		time.sleep(1)
		browser.find_element_by_name("_username").send_keys("admin")
		browser.find_element_by_name("_password").send_keys("123ewq")
		browser.find_element_by_name("_submit").click()
		browser.find_element_by_link_text("Control").click()
		time.sleep(1)
		browser.find_element_by_link_text("Count scores").click()
		self.assertIn("Command Started. Please Wait...", browser.page_source)

	def tearDown(self):
		self.browser.close()

if __name__ == '__main__':
	unittest.main()
