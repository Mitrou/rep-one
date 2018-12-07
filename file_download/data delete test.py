import os
import glob
import shutil
from selenium import webdriver
import time
import zipfile

dwnld_fle_path = r"D:/myGit/rep-one/file_download/file"

# clearing the working space from previous run files
for root, dirs, filenames in os.walk(dwnld_fle_path):
    for filename in filenames:
        filename = os.path.join(root, filename)
        print filename
        if os.path.isfile(filename) is True:
            print "Its a file!"
            print "%s file deleted"%(filename)
        else:
            print "its NOT a file"
        if filename.__contains__("source") or filename.__contains__("target"):
            os.remove(filename)
            print "file deleted"
    print root
    print dirs
    print filenames
