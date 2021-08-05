import string

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
w = 'zaba'

tallest = 0
for i in w:
    position = ord(i) - 97
    tallest = max(tallest, h[position])

print(len(w))
print(tallest)
