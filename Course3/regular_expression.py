import re


# handle = open("mbox-short.txt")
# for line in handle:
#     line = line.strip()
#     if re.search("^From:", line):
#         print(line)
#
# handle = open("mbox-short.txt")
# for line in handle:
#     line = line.strip()
#     if re.search("^X.*:", line):
#         print(line)

# handle = open("mbox-short.txt")
# for line in handle:
#     line = line.strip()
#     if re.search("^X-\s+:", line):
#         print(line)

# x = "My 2 favorite numbers are 19 and 42"
# y = re.findall("[0-9]+", x)
# print(y)
# y = re.findall("[AEIOU]+", x)
# print(y)

# x = "From: Using the : character"
# y = re.findall("^F.+?:", x)
# print(y)

# handle = open("mbox-short.txt")
# for line in handle:
#     y = re.findall('^From (\S+@\S+)', line)
#     if y :
#         print(y)

# handle = open("mbox-short.txt")
# for line in handle:
#     y = re.findall("^From .*@([^ ]*)", line)
#     if y :
#         print(y)

# handle = open("mbox-short.txt")
# numlist = []
# for line in handle:
#     line = line.rstrip()
#     stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
#     # find 0-9 and the period, here . means period not any character
#     if len(stuff) !=1 :
#         continue
#     num = float(stuff[0])
#     numlist.append(num)
# print("Maximum:", max(numlist))

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+?@\S+", x)
print(y)

