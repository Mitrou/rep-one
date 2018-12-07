import os
import glob
import shutil
from selenium import webdriver
import time

# configuring pages for the SOURCE and TARGET data to be downloaded
url_source = "https://support.spatialkey.com/spatialkey-sample-csv-data/"
url_target = "https://support.spatialkey.com/spatialkey-sample-csv-data/"

# configuring profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "C:\\Git\\rep-one\\file_download")
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

# clearing the working space from previous run files
for i in os.listdir('.'):
    if os.path.isfile(i) and (i.startswith("source") or i.startswith("target")):
        os.remove(i)

# open the web page and download the source file
driver = webdriver.Firefox(firefox_profile=fp)
driver.get(url_source)
driver.find_element_by_xpath('//*[@id="post-69"]/div/h5[1]/a').click()
time.sleep(5)
driver.close()

# rename for the following usage as SOURCE
filename = max([f for f in os.listdir('.')], key=os.path.getctime)
shutil.move(os.path.join('.', filename), 'source.csv.zip')

# open the web page and download the target file
driver = webdriver.Firefox(firefox_profile=fp)
driver.get(url_source)
driver.find_element_by_xpath('//*[@id="post-69"]/div/h5[1]/a').click()
time.sleep(5)

# rename for the following usage as TARGET
filename = max([f for f in os.listdir('.')], key=os.path.getctime)
shutil.move(os.path.join('.', filename), 'target.csv.zip')

# closing the driver
driver.close()
