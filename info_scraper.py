from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# Beautiful Soup Object
raw_html = open('source.html',encoding="utf8").read()   
html = BeautifulSoup(raw_html, 'html.parser')

def generate_log(plane_list):
    # Write to Log file for reference  
    file = open("plane.log", "w")
    [ file.write("\n" + line) for line in plane_list ]
    file.close()

def forum_scrape(html):
    # This Function takes a Beuatifulsoup html object and returns a clean list
    # of plane data.  This function was written for a specific forum post.

    # Find the Comment Parent div for Plane Info
    comment = html.find_all("div", {"data-role": "commentContent"})

    # Clean up, strip russian comments
    for line in comment:
    	for row in line.select("div > span"):
    		row.extract()

    # Lists used below
    raw = []
    l_final = []
    l_planes = []

    # Create a list stripping out HTML Tags
    for line in comment:
    	for row in line.stripped_strings:
    		raw.append(row)

    # Clean up comments and surrounding data
    raw.pop(0)
    raw.pop(0)
    raw.pop(len(raw)-1)
    raw.pop(len(raw)-1)

    # Create list of planes to be used to mark them in a future list
    for line in range(len(raw)):
        if "Indicated stall speed in flight configuration:" in raw[line]:
            l_planes.append(raw[line-1])
        elif "Engine" == raw[line]:
            l_planes.append(raw[line-1])

    # Final List that adds markdown to Game and Plane title
    for line in range(len(raw)):
        value = raw[line]

        for row in l_planes:
            if row == raw[line]:
                value = "\n## " + raw[line]

        if "Airplanes of" in raw[line]:
            l_final.append("\n# " + raw[line])
        else:
        	l_final.append(value)

    # Return the Final list
    return l_final

def engine_settings(info):
    pass


# Generate Log of Plane list on exectuion
generate_log(forum_scrape(html))