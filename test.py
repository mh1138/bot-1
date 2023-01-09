from bs4 import BeautifulSoup
import requests


url= "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

print(lists)

for list in lists:
    title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
    location = list.find('div', class_="listing-search-item__location").text.replace('\n', '')
    price = list.find('span', class_="listing-search-item__price").text.replace('\n', '')
    area = list.find('span', class_="illustrated-features__description").text.replace('\n', '')
    
    info = [title, location, price, area]
    print(info)
