import requests

from bs4 import BeautifulSoup

URL = 'https://ridibooks.com/category/new-releases/2200'

response = requests.get(URL)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.title_text')

for number, book in enumerate(bookservices, 1):
    print(number, book.text.strip())
