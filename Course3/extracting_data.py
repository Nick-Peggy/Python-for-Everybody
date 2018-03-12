import re

# f = open("regex_sum_81232.txt")
# numlist = []
# for line in f:
#     line = line.rstrip()
#     a = re.findall("[0-9]+", line)  # find all the numbers in one line
#     if a:
#         for i in range(len(a)):
#             numlist.append(int(a[i]))
#
# print(sum(numlist))

print( sum( [ int(i) for i in re.findall('[0-9]+',open("regex_sum_81232.txt").read()) ] ) )
