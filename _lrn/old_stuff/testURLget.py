# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import re

browser = webdriver.Firefox()                                                  # browser init
browser.get("http://b2lead:Mk18mod0@stg.b2lead.com")
time.sleep(1)

browser.find_element_by_name("_username").send_keys("admin")
browser.find_element_by_name("_password").send_keys("123ewq")
browser.find_element_by_name("_submit").click()

browser.get("http://stg.b2lead.com/admin/b2lead/sendinglist/sendinglist/list?campaignId=50&filter[_sort_order]=DESC&filter[_sort_by]=id&filter[_page]=1&filter[_per_page]=25&filter[campaignId][type]=3&filter[campaignId][value]=0")
browser.find_element_by_link_text("New List").click()
"""browser.find_element_by_name("sendingList[zip_usage_filter]").click()
time.sleep(1)
browser.find_element_by_name("sendingList[zip_usage_filter_list]").send_keys("12312312")
time.sleep(1)
browser.find_element_by_name("sendingList[name]").send_keys("AutotestListname"+time.strftime("%Y-%m-%d"))
browser.find_element_by_name("sendingList[description]").send_keys("Autotest|Listdesc"+time.strftime("%Y-%m-%d"))
time.sleep(1)
browser.find_element_by_id("update_contacts").click()
time.sleep(1)
#selection = browser.find_element_by_id('sendingList_status')
#selection.select_by_value("1").click()"""
el = browser.find_element_by_id('sendingList_status')
print(el)
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Active':
        option.click()










