from smtpd import program


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    root = program.BinaryTree(1)
    root.left = program.BinaryTree(3)
    root.left.left = program.BinaryTree(7)
    root.left.left.left = program.BinaryTree(8)
    root.left.left.left.left = program.BinaryTree(9)
    root.left.right = program.BinaryTree(4)
    root.left.right.right = program.BinaryTree(5)
    root.left.right.right.right = program.BinaryTree(6)
    root.right = program.BinaryTree(2)
    printTree(tree)
    print("-----------------------------------------")
    invertBinaryTree(tree)
    printTree(tree)

main()
