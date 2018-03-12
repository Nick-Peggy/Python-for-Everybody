from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag)
