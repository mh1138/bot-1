import requests
import json
from bs4 import BeautifulSoup


numKey = 0
size_chart = {54: '35.5', 1: '36.0', 13: '36.5', 44: '37.5', 3: '38.0', 48: '38.5', 4: '39.0', 5: '40.0', 22: '40.5', 6: '41.0', 7: '42.0', 23: '42.5', 8: '43.0', 9: '44.0', 24: '44.5', 10: '45.0', 41: '45.5', 11: '46.0', 49: '47.0', 25: '47.5', 21: '48.0', 26: '48.5', 42: '49.5', 28: '50.5', 29: '51.5', 53: '52.5', 2: '37.0', 45: '39.5', 46: '41.5', 52: '46.5', 50: '49.0', 51: '50.0', 85: '51.0', 90: '52.0', 107: '53.0'}


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


#print(search('https://restocks.net/de/shop/search?q=DD1391-100&page=1'))




    

