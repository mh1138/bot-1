import requests
import json
from bs4 import BeautifulSoup


numKey = 0
size_chart = {54: '35 ½', 1: '36', 13: '36 ½', 44: '37 ½', 3: '38', 48: '38 ½', 4: '39', 5: '40', 22: '40 ½', 6: '41', 7: '42', 23: '42 ½', 8: '43', 9: '44', 24: '44 ½', 10: '45', 41: '45 ½', 11: '46', 49: '47', 25: '47 ½', 21: '48', 26: '48 ½', 42: '49 ½', 28: '50 ½', 29: '51 v', 53: '52 ½', 2: '37', 45: '39 ½', 46: '41 ½', 52: '46 ½', 50: '49', 51: '50', 85: '51', 90: '52', 107: '53'}
preis_tabelle = {}
size_price_chart = {}
data = {}

def search(query):
    global size_chart
    global size_price_chart
    global data

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
    }


    html = requests.get(url=query, headers=headers)
    output = json.loads(html.text)
    output_str = str(output)
    data = output['data'][0]
    print(data)
    print(size_chart)

    with open('test.txt', "a") as file:
        file.write(str(size_chart) + "\n")

    def lowest_price():

        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
        url = data['slug']
        print(url)
        

        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        

        for i in size_chart:
            size_id = i
            size = 'size-' + str(size_id)
            lists = soup.find_all('li', id=size)
            if lists == []:
                break
            
            preis = lists[0].find('span', class_='price')
            if preis.text != 'Notify me':
                preis_end = preis.find('span').text
            else:
                preis_end = 'N/A'

            size_price_chart[size_chart[i]] = preis_end




    lowest_price()

    return size_price_chart


# search('https://restocks.net/de/shop/search?q=DD1391-100&page=1')




    

