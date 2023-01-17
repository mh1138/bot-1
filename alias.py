import json
import requests
from cloudscraper import *
import datetime




def search(shoe_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
               'Content-Type': 'application/json'}
    payload = {"requests":[{"indexName":"product_variants_v2",
                         "params":"distinct=true&maxValuesPerFacet=1&page=0&query=" + shoe_id + "&facets=%5B%22instant_ship_lowest_price_cents%22]"}]}
    response = requests.post('https://2fwotdvm2o-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.25.1%3Breact%20(16.9.0)%3Breact-instantsearch%20(6.2.0)%3BJS%20Helper%20(3.1.0)&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a', 
                     headers=headers,
                     json=payload)
    json_data = json.loads(response.text)
    id = json_data['results'][0]['hits'][0]['product_template_id']
    print(id)

    url = f'https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={id}&countryCode=EU'
    print(url)

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    session = requests.Session()

    #html = session.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
    #print(html)
    scraper = CloudScraper.create_scraper()
    html = scraper.get(url=url)
    output = json.loads(html.text)


    size_pricelast = {}
    size_pricelow = {}
    size_pricestock = {}
    for i in range(len(output)):
        variant = output[i]
        if variant['shoeCondition'] == 'new_no_defects' and variant['boxCondition'] == 'good_condition' and variant['stockStatus'] != 'not_in_stock': 
            #print(i, variant['sizeOption']['value'],  variant['stockStatus'], variant['lowestPriceCents']['amount'], variant['lastSoldPriceCents']['amount'])

            size_pricelast[str(variant['sizeOption']['value'])] = variant['lastSoldPriceCents']['amount']/100
            size_pricelow[str(variant['sizeOption']['value'])] = variant['lowestPriceCents']['amount']/100
            size_pricestock[str(variant['sizeOption']['value'])] = variant['stockStatus']
    returndic = [size_pricelast, size_pricelow, size_pricestock]
    return returndic
#print(search('dd1391-100'))