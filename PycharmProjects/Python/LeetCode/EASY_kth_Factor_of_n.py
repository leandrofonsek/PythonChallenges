n = 12
k = 3

list_of_factor = []
for i in range(n):

    actual_number = i + 1
    if n % actual_number == 0:
        list_of_factor.append(actual_number)


if len(list_of_factor) < k:
    print(-1)
else:
    print(list_of_factor[k-1])