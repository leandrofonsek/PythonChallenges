class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertBinaryTree(tree):
    if tree == None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

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

def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.left, level + 1)

def main():
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
    printTree(tree)
    print("-----------------------------------------")
    invertBinaryTree(tree)
    printTree(tree)

main()
