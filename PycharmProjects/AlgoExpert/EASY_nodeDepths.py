class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    node_depth = []
    find_levels(root, 0, node_depth)
    return sum(node_depth)

def find_levels(node, level, node_depth):
    node_depth.append(level)
    if node.left == None and node.right == None:
        return
    if node.left != None:
        find_levels(node.left, level + 1, node_depth)
    if node.right != None:
        find_levels(node.right, level + 1, node_depth)


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
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
    print(nodeDepths(tree))


main()
