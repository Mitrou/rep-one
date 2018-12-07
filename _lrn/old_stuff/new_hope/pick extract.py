# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:49:59 2017

@author: computer_221
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def get_img_url(url):
    browser = webdriver.Chrome()
    browser.set_page_load_timeout(5)
    try:
        browser.get(str(url))
    except TimeoutException:
        browser.execute_script('window.stop();')
        try:
            element = browser.find_element_by_xpath(
                '//*[@id="global-wrap"]/section/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/img')
            print (element)
            url = element.get_attribute('src')
            print (url)
        except NoSuchElementException:
            print ('Fail')


get_img_url('https://dota2.ru/memes/random/')