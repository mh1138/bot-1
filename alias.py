import requests

url = 'https://restocks.net/de/p/nike-dunk-low-retro-white-black-gs'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

html = response.text

print(response)
with open('test.txt', 'w') as f:
    f.write(str(html))