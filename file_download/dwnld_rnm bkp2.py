import os
import glob
import shutil
from selenium import webdriver
import time
import zipfile

# configuring pages for the SOURCE and TARGET data to be downloaded
url_source = "https://support.spatialkey.com/spatialkey-sample-csv-data/"
url_target = "https://support.spatialkey.com/spatialkey-sample-csv-data/"

# configuring profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "C:\\Git\\rep-one\\file_download\\file")
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

# set the download folder path
dwnld_fle_path = r"D:/myGit/rep-one/file_download/file"

# clearing the working space from previous run files
for root, dirs, filenames in os.walk(dwnld_fle_path):
    for filename in filenames:
        filename = os.path.join(root, filename)
        if filename.__contains__("source") or filename.__contains__("target"):
            print "%s file deleted" % (filename)
            os.remove(filename)

# open the web page and download the source file
driver = webdriver.Firefox(firefox_profile=fp)
driver.get(url_source)
driver.find_element_by_xpath('//*[@id="post-69"]/div/h5[1]/a').click()
time.sleep(5)

# rename for the following usage as SOURCE
filename = max([f for f in os.listdir(dwnld_fle_path)], key=os.path.getctime)
shutil.move(os.path.join('.', filename), 'source.csv')

# source unzip
# with zipfile.ZipFile("source.csv.zip", "r") as zip_ref:
#     zip_ref.extractall('.')

# open the web page and download the target file
driver.get(url_target)
driver.find_element_by_xpath('//*[@id="post-69"]/div/h5[1]/a').click()
time.sleep(5)

# closing the driver
driver.quit()

# rename for the following usage as TARGET
filename = max([f for f in os.listdir(dwnld_fle_path)], key=os.path.getctime)
shutil.move(os.path.join('.', filename), 'target.csv')


