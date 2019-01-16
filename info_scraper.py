from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Open and Store Raw Page HTML
raw_html = open('source.html',encoding="utf8").read()

html = BeautifulSoup(raw_html, 'html.parser')

content = html.find("div", {"data-role": "commentContent"})

# Right path so far?
battle = html.find_all("span", {"style": "font-size:20px;"})

comment = html.find_all("div", {"data-role": "commentContent"})
# comment = html.find("div", {"id": "comment-406720_wrap"})

# Clean up, strip russian
for line in comment:
	for row in line.select("div > span"):
		row.extract()

result = []

# The List
for line in comment:
	for row in line.stripped_strings:
		result.append(row)

# Clean up comments surrounding data
result.pop(0)
result.pop(0)
result.pop(len(result)-1)
result.pop(len(result)-1)

[ print(line) for line in result ]
