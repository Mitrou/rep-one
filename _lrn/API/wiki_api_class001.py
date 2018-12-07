import requests
from pelecanus import PelicanJson

# requested data also entry point for processing
# wiki_asked = 'Royal_Military_School_of_Music'


class WikiAPI:
    def wiki_summary_by_name(self,wiki_asked):
        # building link
        link_asked_wiki = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&redirects=1' \
                          '&exintro=&explaintext=&titles=' + wiki_asked

        wiki_response = PelicanJson(requests.get(link_asked_wiki).json())
        # getting a json tree
        for item in wiki_response.enumerate():
            tree_path = item

        # printing wiki content page
        return wiki_response.get_nested_value(tree_path[0])


print(WikiAPI.wiki_summary_by_name('Royal Military School of Music'))