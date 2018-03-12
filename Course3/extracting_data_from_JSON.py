import json
import urllib.request

data = json.loads(urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_81237.json").read())
sum = 0
print(data)
for item in data["comments"]:
    sum = sum + int(item["count"])

print(sum)
