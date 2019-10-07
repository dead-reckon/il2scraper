from requests import get
import csv
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

# This is old, was used to scrape a forum post

# Beautiful Soup Object
raw_html = open('source.html',encoding="utf8").read()   
html = BeautifulSoup(raw_html, 'html.parser')
    

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
        #This else includes planes from Flying Circus
        # elif "Engine" == raw[line]:
        #     l_planes.append(raw[line-1])

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

    # Log out
    file = open("plane.md", "w")
    [ file.write("\n" + line) for line in l_final ]
    file.close()

    # Return the Final list
    return l_final

list_meta = [ "Takeoff speed", 
            "Glideslope speed", 
            "Landing speed" , 
            "Service ceiling", 
            "Dive speed limit",
            "Climb rate at sea level",
            "Climb rate at 3000 m",
            "Climb rate at 6000 m",
            "Flight endurance at 3000 m",
            "Fuel load",
            "Supercharger",
            "Indicated stall speed",
            "Maximum performance turn"]

list_engine = [ "Nominal",
                "Combat power",
                "Emergency power",
                "Boosted power",
                "Take-off power",
                "Max Cruising power",
                "International power",
                "Emergency Max All",
                "Climb power",
                "Model"]

list_speed = [ "Nominal",
                "Combat power",
                "Emergency power",
                "Boosted power",
                "Take-off power",
                "Max Cruising power",
                "International power",
                "Emergency Max All",
                "Climb power",
                "Model"]

def engine_settings(info, search_list):
    file = open("engine.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write(line)
        for row in search_list:
            if re.match(row, line):
                file.write("\n" + line)
    file.close()

def op_features(info):
    file = open("op.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        if re.match('-', line):
            file.write("\n" + line)
    file.close()

def airspeed(info):
    file = open("airspeed.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        if re.match('Maximum true air speed', line):
            file.write("\n" + line)
    file.close()

def oil_water_temp(info):
    file = open("oil_water.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write("\n" + line)
        elif re.match('Oil cap', line):
            pass
        elif re.match('Oil', line) or re.match('Water', line):
            file.write("\n" + line)
    file.close()

def plane_meta(info,search_list):
    # Contains; takeoff/glideslope/landing speeds, dive speed limit, service ceiling, climb rate sea/3k/6k
    file = open("meta.md", "w")

    plane_name = ""

    for line in info:
        if re.search("## ",line):
            file.write(line)
        for row in search_list:
            if re.match(row, line):
                file.write("\n" + line)
    file.close()




# Generate Log of Plane list on exectuion
# generate_log(forum_scrape(html))

plane_meta(forum_scrape(html),list_meta)

op_features(forum_scrape(html))

oil_water_temp(forum_scrape(html))

engine_settings(forum_scrape(html),list_engine)

airspeed(forum_scrape(html))