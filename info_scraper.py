from requests import get

from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# Open and Store Raw Page HTML
raw_html = open('source.html',encoding="utf8").read()

html = BeautifulSoup(raw_html, 'html.parser')

content = html.find("div", {"data-role": "commentContent"})

# all_plane = html.body.find_all("div", {"class": "ipsSpoiler"})

# first_plane = content.span.parent.find_next('p').find_next('p')

# # Find the plane
# plane = content.find("div", {"class": "ipsSpoiler"}).find_previous_sibling('p').find_previous_sibling('p')

# Find all Planes
# plane = content.find_all("div", {"class": "ipsSpoiler"})

# for line in plane:
#     print(line.find_previous_sibling('p').find_previous_sibling('p'))

# [ print(line) for line in plane.stripped_strings ]

# first_content = content.find("div", {"class": "ipsSpoiler_contents"})

# [ print(line) for line in first_content.stripped_strings ]

# Check 
# check_content = dir(content.span)
# [ print(line) for line in check_content ]


# Right path so far?
battle = html.find_all("span", {"style": "font-size:20px;"})

# comment = html.find("div", {"data-role": "commentContent"})
# comment = html.find("div", {"id": "comment-406720_wrap"})

# data = comment.findAll("div", {"class": "ipsSpoiler_contents"})

for line in data:
    print(line)

# for line in battle:
#     # print(line.text)
#     # print(line.find_next("p").find_next("p").text)
    

    # line.find_next("div", {"class": "ipsSpoiler"}).childGenerator




# append
# attrs
# can_be_empty_element
# childGenerator
# children
# clear
# contents
# decode
# decode_contents
# decompose
# descendants
# encode
# encode_contents
# extend
# extract
# fetchNextSiblings
# fetchParents
# fetchPrevious
# fetchPreviousSiblings
# find
# findAll
# findAllNext
# findAllPrevious
# findChild
# findChildren
# findNext
# findNextSibling
# findNextSiblings
# findParent
# findParents
# findPrevious
# findPreviousSibling
# findPreviousSiblings
# find_all
# find_all_next
# find_all_previous
# find_next
# find_next_sibling
# find_next_siblings
# find_parent
# find_parents
# find_previous
# find_previous_sibling
# find_previous_siblings
# format_string
# get
# getText
# get_attribute_list
# get_text
# has_attr
# has_key
# hidden
# index
# insert
# insert_after
# insert_before
# isSelfClosing
# is_empty_element
# known_xml
# name
# namespace
# next
# nextGenerator
# nextSibling
# nextSiblingGenerator
# next_element
# next_elements
# next_sibling
# next_siblings
# parent
# parentGenerator
# parents
# parserClass
# parser_class
# prefix
# preserve_whitespace_tags
# prettify
# previous
# previousGenerator
# previousSibling
# previousSiblingGenerator
# previous_element
# previous_elements
# previous_sibling
# previous_siblings
# recursiveChildGenerator
# renderContents
# replaceWith
# replaceWithChildren
# replace_with
# replace_with_children
# select
# select_one
# setup
# string
# strings
# stripped_strings
# text
# unwrap
# wrap