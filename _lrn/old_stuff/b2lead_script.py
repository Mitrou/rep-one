__author__ = 'SM'
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

browser.get("http://stg.b2lead.com/admin/b2lead/campaign/campaign/list")
time.sleep(1)

browser.find_element_by_link_text("New Campaign").click()                # starting create campaign flow
browser.find_element_by_css_selector("textarea[id*='description']").send_keys("AutotestCampaignDesription"+time.strftime("%Y-%m-%d"))
browser.find_element_by_css_selector("input[id*='name']").send_keys("AutotestCampaignName"+time.strftime("%Y-%m-%d"))
browser.find_element_by_css_selector("input[id*='startDate']").send_keys(time.strftime("%Y-%m-%d"))
browser.find_element_by_css_selector("input[id*='endDate']").send_keys(time.strftime("2015-%m-%d"))
browser.find_element_by_css_selector("input[id*='userCntGoal']").send_keys("3")
browser.find_element_by_name("btn_create_and_edit").submit()                #campaign created
browser.find_element_by_link_text("Content").click()                        #open content tab
time.sleep(1)
browser.find_element_by_link_text("Use").click()                            #take content item as primary
time.sleep(1)
browser.find_element_by_link_text("List").click()
time.sleep(1)
browser.find_element_by_link_text("New List").click()
browser.find_element_by_name("sendingList[zip_usage_filter]").click()                                                   #activate zip field filter
time.sleep(1)
browser.find_element_by_name("sendingList[zip_usage_filter_list]").send_keys("12312312")                                #fill zip field(for one recipient scenario)
time.sleep(1)
browser.find_element_by_name("sendingList[name]").send_keys("AutotestListname"+time.strftime("%Y-%m-%d"))               #fill name field
browser.find_element_by_name("sendingList[description]").send_keys("Autotest|Listdesc"+time.strftime("%Y-%m-%d"))       #fill description field
time.sleep(1)
browser.find_element_by_id("update_contacts").click()               #update button click
time.sleep(1)
el = browser.find_element_by_id('sendingList_status')               #dropdown list selector
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Active':
        option.click()

browser.find_element_by_name("sendingList[save]").click()
time.sleep(2)
browser.find_element_by_link_text("Id").click()
time.sleep(5)
browser.find_element_by_link_text("Use").click()
        #list added into campaign
time.sleep(5)
browser.get("http://stg.b2lead.com/admin/b2lead/campaign/campaign/list?filter[_sort_order]=DESC&filter[_sort_by]=id&filter[_page]=1&filter[_per_page]=25&filter[status][type]=5&filter[status][value]=7")
        #campaign list
browser.find_element_by_link_text("Start").click()
browser.get("http://stg.b2lead.com/admin/manual/do")
browser.find_element_by_link_text("Reset emails per users limitation").click()
time.sleep(5)
browser.get("http://stg.b2lead.com/admin/manual/do")
browser.find_element_by_link_text("Schedule campaigns").click()
time.sleep(5)
browser.get("http://stg.b2lead.com/admin/manual/do")
browser.find_element_by_link_text("Send mails").click()
time.sleep(5)

browser.close()
time.sleep(1)