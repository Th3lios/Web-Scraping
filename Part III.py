#!/usr/bin/python

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# PART III find() and findAll()

# Like scraper you'll also likely want to heavily reuse
# code. Having generic functions such as getSiteHtml and
# getTitle makes it easy to quickly and reliably scrape
# the web

# When Michelangelo was asked how he could sculpt a work
# of art as masterful as his David, he said:
# "It is easy. You just chip away the stone that doesn’t
# look like David.”

# Some method's to extract content aren't effectiv like:

#bsObj.findAll("table")[4].findAll("tr")[2].find("td").findAll("div")[1].find("a")

# Tip:
# Look the information hidden in javascript files. Remember,
# you might need to examine the imported javascript file in
# order to do this.

# Get the content of the span's that have the word green as
# class name

html = urlopen("http:// www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

# Here we use findAll to search all span's with green as class (return a list)
name_list = bsObj.findAll("span",{"class":"green"})

# Print all names of the list
for name in name_list:
    print(name.get_text())

# value.get_text() return a the content as string without any other tag
# in the middle

# find() and findAll() are the 2 functions that you will likely
# use the most. Whit them, you can easyly filter HTML pages.

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# almost 95% of the time you will use just the first 2 arguments

#  function| tag  |         attribute              |
# .findAll("span", {"class":"green", "class":"red"})

# recursive argument is boolean. How deeply into the
# document do you want to go? If recursion is set to
# True, the findAll function looks into children, and
# children’s children, for tags that match your
# parameters.

# By default recursive argument is True

# text argument is used to find a specific string in tags

# limit argument is only used in findAll. limit 1 is equal
# to find()
# limit is used to return just the first x items from the pageç

# keyword argument allows you to select tags that contain
# a particular attribute

allText = bsObj.findAll(id="text")
print(allText[0].get_text())

# The keyword is redundant in BS because exist regular expressions
# for that


# In beautifulsoup exist other objects
# BeautifulSoup objects (BeautifulSoup function return this)
# Tags objects
# NavigableString objects (Find's functions return this)
# Comment object

# .childen find only descendants that are children
# All children are decendants, but not all decendants are children

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table",{"id":"giftList"}).children:
print(child)

# You can un descendants() to only find descendants

# Children's are tags that are exactly below a parent
# Descendant's are tags of any level below

# next_siblings() return a list of tag siblings

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

# also exist previous_sibling

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# return the brother content of the father of img tag



