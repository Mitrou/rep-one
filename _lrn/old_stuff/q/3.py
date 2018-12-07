from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("http://b2lead:Mk18mod0@stg.b2lead.com")
wait_cron = WebDriverWait(webdriver, 130)
browser.find_element_by_name("_username").send_keys("admin")
browser.find_element_by_name("_password").send_keys("123ewq")
browser.find_element_by_name("_submit").click()
browser.get("http://stg.b2lead.com/admin/manual/do")
browser.find_element_by_link_text("Reset emails per users limitation").click()
wait_cron.until(ec.text_to_be_present_in_element(By.CSS_SELECTOR, "where updated"))
browser.get("http://stg.b2lead.com/admin/manual/do")

wait = WebDriverWait(webdriver, 10)
element = wait.until(ec.element_to_be_clickable((By.ID,'someid')))