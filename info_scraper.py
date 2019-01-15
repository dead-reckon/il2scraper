from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Open and Store Raw Page HTML
raw_html = open('source.html',encoding="utf8").read()

html = BeautifulSoup(raw_html, 'html.parser')

content = html.find("div", {"class": "cPost_contentWrap ipsPad"})

# all_plane = html.body.find_all("div", {"class": "ipsSpoiler"})

first_plane = content.span.parent.find_next('p').find_next('p')

# Find the plane
# plane = content.find("div", {"class": "ipsSpoiler"}).find_previous_sibling('p').find_previous_sibling('p')

# Find all Planes
plane = content.find_all("div", {"class": "ipsSpoiler"}).find_next_siblings()



for line in plane:
    print(line)

# for line in plane:
#     print(line.find_previous_sibling('p').find_previous_sibling('p'))

# [ print(line) for line in plane.stripped_strings ]

# first_content = content.find("div", {"class": "ipsSpoiler_contents"})

# [ print(line) for line in first_content.stripped_strings ]

# Check 
check_content = dir(content.span)
[ print(line) for line in check_content ]
