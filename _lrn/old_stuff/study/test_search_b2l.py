__author__ = 'User'

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()                                                  # browser init
browser.get("http://b2lead:Mk18mod0@stg.b2lead.com")
time.sleep(1)

browser.find_element_by_name("_username").send_keys("admin")
browser.find_element_by_name("_password").send_keys("123ewq")
browser.find_element_by_name("_submit").click()

browser.get("http://stg.b2lead.com/admin/b2lead/campaign/campaign/list")
browser.find_element_by_css_selector("html body.sonata-bc div.wrapper div.top-menu div.menu-sub-action div.search-block input").send_keys(time.strftime("%Y-%m-%d")).send_keys(Keys.ENTER)