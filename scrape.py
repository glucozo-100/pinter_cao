import requests
import pandas as pd
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
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html5lib')
    
    comment_count = soup.find("h2", {'class': 'lH1 dyH iFc H2s bwj X8m zDA IZT'})
    comment_count = comment_count.text if comment_count else 'Comments not found'
    
    author = soup.find('div', {'class': 'tBJ dyH iFc sAJ X8m zDA IZT H2s'}, {'dataset_id': 'creator-profile-name'})
    if author is None:
        author = soup.find('div', {'class': 'tBJ dyH iFc j1A X8m zDA IZT H2s'}, {'dataset_id': 'creator-profile-name'})
    author = author.text if author else 'Author not found'
    
    follower = soup.find('div', {'data-test-id': 'user-follower-count'})
    if follower is not None:
        followers = follower.find('div', {'class': 'tBJ dyH iFc sAJ X8m zDA IZT swG'})
        followers_text = followers.get_text(strip=True) if followers else 'Followers not found'
    else:
        follower = soup.find('div', {'data-test-id': 'follower-count'}, {'class':'tBJ dyH iFc sAJ X8m zDA IZT swG'})
        followers_text = follower.text if follower else 'Follower count not found'
    
    return author, followers_text, comment_count

def main():
    data = pd.read_csv('data.csv')
    results = []

    for index, row in data.iterrows():
        url = row['url']
        name = row['name']
        author, follower, comment_count = get_pinterest_links(url)
        results.append({
            'name': name,
            'url': url,
            'author': author,
            'follower': follower,
            'comment_count': comment_count
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv('anime.csv', index=False)

if __name__ == "__main__":
    main()
