#scraping the web

import requests

from bs4 import BeautifulSoup


url = 'https://stockx.com/sell/air-jordan-1-retro-high-og-chicago-reimagined-lost-and-found'

headers = {
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }


page = requests.get(url=url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
with open('test.txt', 'w') as f:
    f.write(str(soup))
lists = soup.find_all('div', class_="css-1pk7u7p")

print(lists)

for list in lists:
    Grösse = list.find('p', class_='css-1aoneeq')
    Preis = list.find('p', class_='css-1ogfskg')
    info = [Grösse, Preis]
    print(info)