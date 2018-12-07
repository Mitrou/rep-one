__author__ = 'User'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Firefox()
driver.get("http://selenium-python.readthedocs.org/en/latest/faq.html")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")