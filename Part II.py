#!/usr/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup

bsObj = BeautifulSoup(html.read())

# PART II EXCEPTIONS

# In web scraping is normal that the scrap fail for a change
# in the web page or any 404 error or 500, therefor you
# need to use exceptions.

# With this you prevent any HTTP error code.
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    pass


if html is None:
    print("Url is not found")
else:
    pass

# Some times the pages don't have the tag that you
# want to search, therefor you need to catch the
# AttributeError

# print(bsObj.non_existent_tag)
# If you don't check this ↑, the program will stop

try:
    bad_content = bsObj.non_existent_tag
except AttributeError as e:
    print("Tag was not found")
else:
    pass

if bad_content == None
    print("Tag was not found")
else:
    print(bad_content)

######### EXAMPLE ###########

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1 except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

##############################