def twoNumberSum(array, targetSum):
    # Write your code here.

    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] + array[j] == targetSum:
                return (array[i], array[j])

    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    print(twoNumberSum(array, 10))

main()
