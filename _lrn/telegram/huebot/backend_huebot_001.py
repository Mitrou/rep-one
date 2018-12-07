import requests
from pelecanus import PelicanJson
from bs4 import BeautifulSoup

# requested data also entry point for processing


class WikiAPI:
    def wiki_summary_by_name(self):
        # building link
        link_asked_wiki = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&redirects=1' \
                          '&exintro=&explaintext=&titles=' + str(self)
        wiki_response = PelicanJson(requests.get(link_asked_wiki).json())
        # getting a json tree
        for item in wiki_response.enumerate():
            tree_path = item
        # printing wiki content page
        return wiki_response.get_nested_value(tree_path[0])

    def wiki_refer_to(self):
        rslt_list = ''
        # building link
        link_asked_wiki = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&redirects=1' \
                          '&titles=' + str(self)
        soup = BeautifulSoup(requests.get(link_asked_wiki).text, "html.parser")
        for lis in soup.findAll('li'):
            if "All pages" not in lis.get_text():
                rslt_list += str(lis.get_text()) + '\n'
        return rslt_list




