import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPDigestAuth, HTTPBasicAuth
import pprint
domain = "https://dedmorozural.ru"

url = f"{domain}/novosti/page-1"

headers = {
    'Host': 'dedmorozural.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'InstantCMS[logdate]=1673687071; _ym_uid=1673120949313680793; _ym_d=1673120949; PHPSESSID=817df77ddff7edeb108070c34387509d; _ym_isad=2; InstantCMS[userid]=961d3acb5a3da1c05e54b77a8232a715',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

span = soup.find("span", class_="register")
print(span)

span = soup.find("span", class_="my_profile")
print(span)

result = {}

teg_a = soup.find_all("a", class_="con_titlelink")
for one_news_a in teg_a:
    text = one_news_a.text
    href = one_news_a.get("href")
    # print(text, href)

    # Шаг второй (формируем новый url)
    url = f"{domain}{href}"
    response = requests.get(url)
    soup_1 = BeautifulSoup(response.text, 'html.parser')
    # Получаем заголовки
    news_titles_tag = soup_1.find_all("strong")
    titles = []
    for title_tag in news_titles_tag:
        # print(title_tag.text)
        titles.append(title_tag.text)
    # Добавим в словарь
    result[text] = titles

pprint.pprint(result)
