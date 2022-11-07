import requests
from bs4 import BeautifulSoup


URL = 'https://www.sindppd-rs.org.br/'

KEYWORDS = [
    'oposição',
    'oposições',
    'CONTRIBUIÇÃO',
    'ASSISTENCIAL',
    'CONTRIBUIÇÃO ASSISTENCIAL'
]

def search_matching_posts(url: str, keywords: list[str]): 
    res = requests.get(url)

    if res.status_code != 200:
        raise Exception(f'"{url}" return status code <{res.status_code}>')

    soup = BeautifulSoup(res.text, 'html.parser')
    recent_posts_ul = soup.find(text="Últimas Notícias").parent.parent.ul
    posts_li = recent_posts_ul.findAll('li')

    matching_posts_url = []
    for li in posts_li:
        if any(word.lower() in li.a.text.lower() for word in keywords):
            matching_posts_url.append({
                'href': li.a['href'],
                'text': li.a.text
            })

    return matching_posts_url


if __name__ == '__main__':
    matching_posts = []
    try:
        matching_posts = search_matching_posts(URL, KEYWORDS)
    except:
        print('Script is not properly working. The webpage has been updated or the server is offline.')
        exit(1)
    
    if len(matching_posts) == 0:
        print('There is no matching posts with provided keywords')
        exit(0)
    
    print(matching_posts)
