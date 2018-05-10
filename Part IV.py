#!/usr/bin/python

# First of all, do this:
# import re
# Part IV Regular Expression's
# Regular expressions are so called because they are
# used to identify regular strings.

# “Yes, this string you’ve given me follows the rules, and I’ll return it,”
# “This string does not follow the rules, and I’ll discard it.”

# Regular string: It's any string that can be generate by a series of linear
# rules, such as:

# 1. Write the letter “a” at least once.
# 2. Append to this the letter “b” exactly five times.
# 3. Append to this the letter “c” any even number of times.
# 4. Optionally, write the letter “d” at the end.

# Result: “aaaabbbbbccccd,” “aabbbbbcc,”

# a* means "any number of a's, including 0 of them
# (cc)* "any number of pairs of c's, including 0 pairs"
# (d|) means "add a d followed by a space or just add a space without a d"

# *     Matches the preceding character. 0 or more times. (a*b*)
# +     Matches the preceding character. 1 or more times. (a+b+)
# []    Matches any character within the brackets. ([A-Z])
# ()    A grouped subexpression. evaluated in order of operations. (a*b)*
# {m,n} Matches the preceding character between m and n times. a{2,3}b{2,3}
# [^]   Matches any single character that is not in the brackets. [^A-Z]*
# |     Matches any character or string separated by the |. b(a|i|e)d / bad bid bed
# .     Matches any single character. b.d / bad bid bed bzd bxd b?d...
# ^     Indicate tht a character occurs at the beginning of a string ^a / apple
# \     This allow you to use "special" character as their literal meaning (\.)
# $     Often used at the end of a regular expression (a$) carta/bbaa
# ?!    "Does not contain" indicate that that character should't be found

# Example:

from urllib.request
import urlopenfrom bs4
import BeautifulSoupimport re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) for image in images:
print(image["src"])

# Results
# ../img/gifts/img1.jpg
# ../img/gifts/img2.jpg
# ../img/gifts/img3.jpg
# ../img/gifts/img4.jpg
# ../img/gifts/img6.jpg

# In BS exist an object named "tag objects", and you can access to his
# attributes content with .attrs

# myTag.attrs
# myImgTag.attrs['src]

# Lambda Expressions

# Lambda expression is a "function" "that is passed into another" "function"
# as a variable; that is, instead of defining a function as f(x, y),
# you may define a function as f(g(x), y), or even f(g(x), h(x)).

# The only restriction is that these functions must take a "tag object"
# as an argument and return a boolean.
# Example

soup.findAll(lambda tag: len(tag.attrs) == 2)

# retrieves all tags that have exactly two attributes
# That is, it will find tags such as the following:
# <div class="body" id="content"></div>
# <span style="color:red" class="title"></span>

# Using lambda functions in BeautifulSoup, selectors
# can act as a great substitute for writing a regular
# expression, if you’re comfortable with writing a little code.
