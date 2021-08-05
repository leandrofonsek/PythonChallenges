def isValidSubsequence(array, sequence):
    # Write your code here.

    elements_matching = 0
    for value in array:
        if elements_matching == len(sequence):
            break
        if sequence[elements_matching] == value:
            elements_matching += 1

    return elements_matching == len(sequence)





def main():
    array = [1, 2, 3, 4, 5, 6]
    sequence = [1, 5, 6]

    print(isValidSubsequence(array, sequence))
main()
