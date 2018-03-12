handle = open("mbox-short.txt")
counts = {}
for line in handle:
    if line.startswith("From "):
        a = line.rstrip().split()
        a = a[5].split(":")
        counts[a[0]] = counts.get(a[0], 0)+1

lst = sorted(counts.items())
for val, key in lst:
    print(val, key)