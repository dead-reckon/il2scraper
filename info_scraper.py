from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Open and Store Raw Page HTML
raw_html = open('source.html',encoding="utf8").read()

html = BeautifulSoup(raw_html, 'html.parser')

head_tag = html.head

title_tag = head_tag.contents[1]


# print(title_tag)
# print(head_tag.contentss)

print()

# Lists everything
# for string in html.stripped_strings:
#     print(string)