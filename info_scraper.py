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



content = html.find("div", {"class": "cPost_contentWrap ipsPad"})

# all_plane = html.body.find_all("div", {"class": "ipsSpoiler"})

first_plane = content.span.parent.find_next('p').find_next('p')

print(first_plane.text.strip())

first_content = content.find("div", {"class": "ipsSpoiler_contents"})

for line in first_content.stripped_strings:
    print(line)

# Check 
# check_content = dir(content.span)
# [ print(line) for line in check_content ]
