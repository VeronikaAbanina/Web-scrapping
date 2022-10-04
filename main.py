import bs4
import requests
import fake_headers

KEYWORDS = ['Mathematics *', 'IT-companies', 'Web design *', 'Game development *']

HEADERS = ''

URL = 'http://habr.com'

response = requests.get(URL, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features = 'html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = [hub.text.strip() for hub in hubs] #list comprexensions
    for hub in hubs:
        if hub in KEYWORDS:
            date = article.find(class_='tm-article-snippet__datetime-published').text
            title = article.find('h2').find('span').text
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            result = f'{date} – {title} – {URL}{href}'
            print(result)