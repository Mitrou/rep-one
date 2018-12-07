__author__ = 'SM'
# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import re

browser = webdriver.Chrome()                                                  # browser init
browser.get("http://google.com")
browser.get_screenshot_as_file("C:\_screens\scr.png")
browser.get_screenshot_as_png()
browser.close()