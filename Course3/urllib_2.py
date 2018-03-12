import urllib.request, urllib.parse, urllib.error

f = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = {}
for line in f:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)