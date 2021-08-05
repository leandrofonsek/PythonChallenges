"""
Given an integer array arr, return the mean of the remaining integers after removing the
smallest 5% and the largest 5% of the elements.
Answers within 10-5 of the actual answer will be considered accepted.
"""

arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
arr.sort()

five_percent = len(arr) * 5 / 100
total_size = int(len(arr) - 1)

for x in range(int(five_percent)):
    arr.pop(x)
    arr.pop()

sum = 0
count = 0
for x in arr:
    sum = sum + x
    count = count + 1

print(sum/count)