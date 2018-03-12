import numpy as np

fh = open("1.txt")
lst = list()
for line in fh:
    a = line.rstrip().split(" ")
    for i in a:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
