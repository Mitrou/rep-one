import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'

headers = {
    'User-Agent': user_agent,
}

url = 'https://dota2.ru/memes/random/'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.select('div.wall div img')[0].get('src'))