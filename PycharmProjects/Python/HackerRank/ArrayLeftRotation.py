def isBalanced(s):
    stack = []
    balancedPairs = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i in balancedPairs.values():
            stack.insert(0, i)
        elif not stack:
            return "NO"
        elif stack[0] == balancedPairs[i]:
            del stack[0]
        else:
            return "NO"

    if stack:
        print(stack)
        return "NO"

    return "YES"

def main():
    s = "}][}}(}][))]"
    print(isBalanced(s))
main()