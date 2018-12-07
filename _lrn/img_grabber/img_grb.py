from variables import *
import requests
from bs4 import BeautifulSoup
import os.path
import time

# getting timestamp
timestp = time.strftime("%Y%m%d-%H%M%S")
# generating final path
f_path = save_path + timestp
# initial page GET
r = requests.get(url_4_grb)
if not os.path.exists(f_path):
    os.makedirs(f_path)
# data reassembling
data = r.text
# getting page structure with soup
soup = BeautifulSoup(data, "html.parser")
# taking all <a class "desktop"
for link in soup.find_all("a", {"class": "desktop"}):
    # deleting all before ? symbol and adding beginning of a link
    question_mark = link.find("?")
    raw_image = "https://2ch.hk" + link.get("href")[:question_mark]
    # filtering desired content and downloading in particular folder
    # means not in string
    if raw_image.find("src") != -1:
        # combining full file name including initial file extension,
        # path for saving, and inappropriate symbols replacement
        completeName = os.path.join(f_path, raw_image.replace(":", "").replace("/", "--"))
        # image download instance
        r2 = requests.get(raw_image)
        # writing in a file
        with open(completeName, "wb") as f:
            f.write(r2.content)
            f.close()
