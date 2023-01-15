import json
import requests

shoe = {'styleID':'DD1391-100'}


def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
               'Content-Type': 'application/json'}
    payload = {"requests":[{"indexName":"product_variants_v2",
                         "params":"distinct=true&maxValuesPerFacet=1&page=0&query=" + shoe['styleID'] + "&facets=%5B%22instant_ship_lowest_price_cents%22]"}]}
    response = requests.post('https://2fwotdvm2o-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.25.1%3Breact%20(16.9.0)%3Breact-instantsearch%20(6.2.0)%3BJS%20Helper%20(3.1.0)&x-algolia-application-id=2FWOTDVM2O&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a', 
                     headers=headers,
                     json=payload)
    json_data = json.loads(response.text)
    id = json_data['results'][0]['hits'][0]['product_template_id']
    print(id)

    url = f'https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={id}'
    print(url)

    headers = {
            'authority': 'www.goat.com',
            'method': 'GET',
            'path': '/web-api/v1/product_variants/buy_bar_data?productTemplateId=719082',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': '_csrf=GQnsvvfMbT0HGKFx0udmXTHT; guestCheckoutCohort=49; global_pricing_regions={"AT":"2","BE":"2","BG":"2","CY":"2","CZ":"2","DE":"2","DK":"2","EE":"2","ES":"2","FI":"2","FR":"2","GR":"2","HK":"223","HR":"2","HU":"2","IE":"2","IT":"2","JP":"57","LT":"2","LU":"2","LV":"2","MT":"2","MY":"69","NL":"2","PL":"2","PT":"2","RO":"2","SE":"2","SG":"106","SI":"2","SK":"2","UK":"4","US":"3"}; currency=USD; country=US; ConstructorioID_client_id=4be43cfe-2193-451c-abce-68d53b386aff; global_pricing_id=3; ConstructorioID_session_id=2; tracker_device=aedfcb4e-2321-4b62-8430-d613a68b193f; amp_365902=T_uTjUX8ICD0XZXUWtsw_r...1gmqvianb.1gmqviang.0.1.1; __cf_bm=WTzKQax7CudRYV990jx2ZrNRSZJhEFwMS1cGChPOdmI-1673795354-0-ARe+oq0XM+OUIlki35nmsrJzXNwFBxz40fh66pndoCoSDpNo6PDSb0UboPvfYUuOae2bYnlPfWsGYKKbpo3QMzo=; ConstructorioID_session={"sessionId":2,"lastTime":1673795364318}; OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+15+2023+16%3A09%3A25+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=6.10.0&hosts=&consentId=66cb9f61-a91c-4116-9611-51ab27d6068f&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; csrf=7qwhTPHy-K_0FYbLkP4K9mIwnTkaVSKozEn0',
            'if-none-match': 'W/"d3f0-V8OgkZ+Z/kEJ/294CB/LnIVeAqg"',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
          }

    headers = {
        'accept': 'application/json',
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

    html = requests.get(url=url, headers=headers)

    print(html)

main()