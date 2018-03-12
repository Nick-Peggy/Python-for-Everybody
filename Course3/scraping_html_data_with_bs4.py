from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

url = "http://py4e-data.dr-chuck.net/comments_81234.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
tags = soup("span")
num = 0
for tag in tags:
    num = num + int(re.findall("[0-9]+", str(tag))[0])

print(num)
