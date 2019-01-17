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

raw = []

# The List
for line in comment:
	for row in line.stripped_strings:
		raw.append(row)

# raw = [ row for row in line.stripped_strings for line in comment ]

# Clean up comments surrounding data
raw.pop(0)
raw.pop(0)
raw.pop(len(raw)-1)
raw.pop(len(raw)-1)

l_final = []
l_planes = []

# for line in range(len(raw)):
#     if "Indicated stall speed in flight configuration:" in raw[line]:
#         final.insert((line-1), "\n####")
#     elif "Engine" == raw[line]:
#         final.insert((line-1), "\n####")
#     # elif "Airplanes of" in raw[line] and line != 0:
#     #     final.insert((line-1), "\n====")
#     final.append(raw[line])

for line in range(len(raw)):
    if "Indicated stall speed in flight configuration:" in raw[line]:
        l_planes.append(raw[line-1])
    elif "Engine" == raw[line]:
    	l_planes.append(raw[line-1])

for line in range(len(raw)):
    for row in l_planes:
    	if row == raw[line]:
    		l_final.append("\n## " + raw[line])

    if "Airplanes of" in raw[line]:
        l_final.append("\n# " + raw[line])
    else:
    	l_final.append(raw[line])
    

[ print(line) for line in l_final ]

# final = []

# for line in range(len(step1)):
#     if "Airplanes of" in step1[line]:
#         # final.insert((line+1), "\n====")
#         print(line)
#     else:
#         final.append(step1[line])

# [ print(line) for line in final ]
