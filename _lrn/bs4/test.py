from bs4 import BeautifulSoup
import requests

rslt = ''
link_asked_wiki = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&redirects=1' \
                  '&titles=edd'
soup = BeautifulSoup(requests.get(link_asked_wiki).text, "html.parser")
for lis in soup.findAll('li'):
    if "All pages" not in lis:
        rslt += str(lis.get_text()) + '\n'
print(rslt)
