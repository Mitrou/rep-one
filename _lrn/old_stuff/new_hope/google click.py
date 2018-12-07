import unittest
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com.ua/")
driver.find_element_by_name("q").send_keys("wix")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
time.sleep(3)
asd = driver.find_elements_by_class_name('r')[2]
asd.click()
# asd = asd.get_attribute('href')
# driver.get(asd)
time.sleep(5)
# print(asd)
# driver.quit()