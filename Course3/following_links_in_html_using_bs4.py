from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

position = 18
count = 7
url = "http://py4e-data.dr-chuck.net/known_by_Julita.html"
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = re.findall("href=\"(.*)\"", str(tags[position - 1]))[0]
    print(url)



