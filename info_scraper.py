from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Open and Store Raw Page HTML
raw_html = open('source.html',encoding="utf8").read()

html = BeautifulSoup(raw_html, 'html.parser')

for line in html.select('div'):
    if line['class'] == "ipsSpoiler":
        print(p.text)