class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums_list = []
    calculateSum(root, 0, sums_list)
    return sums_list


def calculateSum(node, branch_sum, sums_list):
    # If node exists, add its value to the branch sum
    branch_sum = branch_sum + node.value

    # If the node is a leaf, we are done on this branch, append
    # the branch_sum to the list and exit
    if node.left == None and node.right == None:
        sums_list.append(branch_sum)

    # If it got here, it means the branch still has, at least,
    # one node on the branch to be calculated
    if node.left != None:
        calculateSum(node.left, branch_sum, sums_list)

    if node.right != None:
        calculateSum(node.right, branch_sum, sums_list)


class BinaryTree(Node):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def main():
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    print(branchSums(tree))


main()
