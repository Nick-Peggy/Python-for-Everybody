import urllib.request
import xml.etree.ElementTree as ET

f = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_81236.xml')
stuff = ET.fromstring(f.read())
lst = stuff.findall("comments/comment")
sum = 0
for item in lst:
    sum = sum + int(item.find("count").text)

print(sum)