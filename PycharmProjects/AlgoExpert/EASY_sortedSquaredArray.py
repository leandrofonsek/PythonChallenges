def sortedSquaredArray(array):
    # Write your code here.

    return_array = []
    for i in array:
        return_array.append(i*i)
    return_array.sort()
    return return_array

def main ():

    array = [1, 2, 4, 8, 16]
    print(sortedSquaredArray(array))

main()