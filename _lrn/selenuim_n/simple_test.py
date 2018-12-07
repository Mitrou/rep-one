from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# configuring profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "C:\\Git\\rep-one\\file_download")
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')


driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
