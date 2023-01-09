import requests
import json


numKey = 0
size_chart = {}


def search(query):
    global size_chart

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://restocks.net/de/account/sell',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }


    html = requests.get(url=query, headers=headers)
    output = json.loads(html.text)
    output = str(output)
    part1, part2 = output[:18], output[13:]

    number = part2.split()[1]

    url = f'https://restocks.net/de/product/get-sizes/{number}'

    url = url.replace("'", "")
    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)

    for key in output:
        size_chart[key['id']] = key['name']

    print(size_chart)



    def lowest_price(size):

        headers1 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br, UTF-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://restocks.net/de/product/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }


        for i in size_chart:
            if size_chart[i]==size:
                value = i 

        size_url = f'https://restocks.net/de/product/get-lowest-price/{number}/{value}'
        size_url = size_url.replace("'", "").replace(",", "")
        print(size_url)

        test = requests.get(url=size_url, headers=headers1)
        print(test.raw)
    lowest_price('36')

search('https://restocks.net/de/shop/search?q=dd1391-100&page=1')
    

