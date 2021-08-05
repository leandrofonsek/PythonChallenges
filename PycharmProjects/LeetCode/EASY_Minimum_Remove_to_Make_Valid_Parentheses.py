"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""

#turning string into array
s = "(a(b(c)d)"
s_array = list(s)
#print(s_array)

opened_parentheses=0
closed_parentheses=0
s_array_new=[]
for i in range(len(s_array)):

    if s_array[i] == "(":
        opened_parentheses = opened_parentheses + 1

    if s_array[i] == ")":
        if opened_parentheses == 0:
            continue
        else:
            closed_parentheses = closed_parentheses + 1

    s_array_new.append(s_array[i])

#print("Opened: " + str(opened_parentheses))
#print("Closed: " + str(closed_parentheses))

diff_parentheses = opened_parentheses - closed_parentheses
#print(diff_parentheses)

s_array=[]
if diff_parentheses == 0:
    print(s)
elif diff_parentheses > 0:
    for i in range(len(s_array_new)):

        if diff_parentheses != 0 and s_array_new[i] == "(":
            diff_parentheses = diff_parentheses - 1
            continue

        s_array.append(s_array_new[i])

else:
    diff_parentheses = diff_parentheses * -1
    print("More closed than opened")

    for i in range(len(s_array_new)):

        if diff_parentheses != 0 and s_array_new[i] == ")":
            diff_parentheses = diff_parentheses - 1
            continue

        s_array.append(s_array_new[i])

output = ""
for x in s_array:
        output += x
print(output)