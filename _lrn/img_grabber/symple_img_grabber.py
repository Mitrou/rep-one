import requests
from bs4 import BeautifulSoup
import os.path


# url for grabbing is an artist tread on 2ch
url_4_grb = "http://korrespondent.net/"

# file path for saving
save_path = r"D:\myGit\rep-one\_lrn\img_grabber\grabbed"

# initial page GET
r = requests.get(url_4_grb)
# data reassembling
data = r.text
# getting page structure with soup
soup = BeautifulSoup(data, "html.parser")
# taking all <a class "desktop"
for link in soup.find_all("img"):
    # deleting all before ? symbol and adding beginning of a link
    question_mark = link.find("?")
    raw_image = link.get("src")[:question_mark]
    # filtering desired content and downloading in particular folder
    # means not in string
    if raw_image.find("http") != -1:
        #     combining full file name including initial file extension,
        #     path for saving, and inappropriate symbols replacement
        completeName = os.path.join(save_path, raw_image.replace(":", "").replace("/", "--").
                                    replace("?", "wut").replace("&", "and"))
        print(raw_image)
        # image download instance
        r2 = requests.get(raw_image)
        # writing in a file
        with open(completeName, "wb") as f:
            f.write(r2.content)
            f.close()
        print("file downloaded")
