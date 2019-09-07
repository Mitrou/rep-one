from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# configuring profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "C:\\Git\\rep-one\\file_download")
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')



driver = webdriver.Firefox(firefox_profile=fp)
wait = WebDriverWait(driver, 10)
driver.get("https://rozetka.com.ua/")
driver.find_element_by_link_text('увійдіть в особистий кабінет').click()
# wait.until(EC.visibility_of_element_located((By.ID, 'auth_email')))
sleep(1)
driver.find_element_by_id('auth_email').send_keys('mahnosam@gmail.com')
driver.find_element_by_id('auth_pass').send_keys('gtkmvtyb')
driver.find_element_by_css_selector('button.button_color_navy:nth-child(1)').click()
