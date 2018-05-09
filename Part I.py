#!/usr/bin/python

# PART I Install and test

# This tutorial will use BeautifulSoup Package
# pip install beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Return an object
html = urlopen("http://www.pythonscraping.com/pages/page1.html")

# html.read() return de html content
bsObj = BeautifulSoup(html.read(), "html.parser")

# Show the content of the tag h1
print(bsObj.h1)
