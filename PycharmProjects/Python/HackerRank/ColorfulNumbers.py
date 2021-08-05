n = [ 3, 2, 4, 5 ]
#n = [ 3, 2, 6 ]
temp = []

for i in range(len(n)):
    #print("i = {}".format(i))
    for j in range(i, len(n)):
        #print("   j = {}".format(j))
        #print("   n[i:j+1] = {}".format(n[i:j + 1]))
        temp.append(n[i:j + 1])

map = {}
for array in temp:

    if len(array) == 1:
        result = array[0]
    else:
        result = 1
        for i in array:
            result = result * i

    if map.has_key(result):
        print("Not colorful, found {} twice".format(result))
        break
    else:
        map[result] = 1

print(map)
