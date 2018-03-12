import urllib.request, urllib.parse, urllib.error, re

f = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in f:
    link = re.findall("href=\"(.+)\"", line.decode().strip())
    if len(link) != 0:
        print(link[0])
