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
# asd = driver.find_elements_by_tag_name('a')
asd = driver.find_elements_by_class_name('r')
for i in asd:
    i = i.get_attribute('href')
    print(i)
driver.quit()
