import requests
from bs4 import BeautifulSoup

def get_pinterest_links(url):
    headers = {
    'accept': 'application/json, text/javascript, */*, q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.pinterest.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.89", "Chromium";v="127.0.6533.89"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-app-version': 'f4e841d',
    'x-pinterest-appstate': 'background',
    'x-pinterest-pws-handler': 'www/pin/[id].js',
    'x-pinterest-source-url': '/pin/1970393580411909/',
    'x-requested-with': 'XMLHttpRequest',
}
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    with open('soup.txt', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    href = soup.find_all('img')
    print(href)
    

    
url = 'https://www.pinterest.com/search/pins/?q=one%20piece&rs=typed'


pin_links = get_pinterest_links(url)


