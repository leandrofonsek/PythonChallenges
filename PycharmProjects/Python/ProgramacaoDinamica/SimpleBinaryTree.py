# https://www.youtube.com/watch?v=6E169kShoNU
# https://www.youtube.com/watch?v=GleEQPKxlPg
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level + 1)

    def inorder_traversal(self, node=None):
        # print order: left node data, current node data, right node data
        if node == None:
            node = self.root
        # print: left node
        if node.left:
            self.inorder_traversal(node.left)
        # print: current node
        print(node)
        # print: right node
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        # print order: left node data, current node data, right node data
        if node == None:
            node = self.root
        # print: left node
        if node.left:
            self.postorder_traversal(node.left)
        # print: right node
        if node.right:
            self.postorder_traversal(node.right)
        # print: current node
        print(node)

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(right_height, left_height)

    def diameter(self, node=None):
        if node is None:
            return [0, 0]

        left_node_info = self.diameter(node.left)
        right_node_info = self.diameter(node.right)

        longest_path_through_current_node = left_node_info[0] + right_node_info[0]
        diameter_from_child_nodes = max(left_node_info[1], right_node_info[1])
        # IF the current node is the root of the biggest diameter,then the sum of his child heights will be bigger
        #  than the biggest diamenter found so far.
        diameter = max(longest_path_through_current_node, diameter_from_child_nodes)
        current_node_height = 1 + max(left_node_info[0], right_node_info[0])

        return [current_node_height, diameter]


class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        current_node = self.root
        while (current_node):
            parent = current_node
            if value < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return value
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def searchClosest(self, value):
        return self._searchClosest(value, self.root)

    def _searchClosest(self, value, node,i=0,closest=0,diff=0):
        if node is None:
            return closest
        if node.data == value:
            return value
        if i == 0:
            closest = node.data
            diff = abs(value - node.data)
            i = 1
        else:
            if abs(value - node.data) < diff:
                closest = node.data
                diff = abs(value - node.data)
        if value < node.data:
            return self._searchClosest(value, node.left,i,closest,diff)
        return self._searchClosest(value, node.right,i,closest,diff)

def main():
    tree = BinaryTree(0)
    tree.root.left = Node(1)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.left.right.left = Node(10)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.right.left = Node(7)

    print("")
    tree.printTree(tree.root)

    print("-----------------------")
    print("Inorder Traversal")
    tree.inorder_traversal(tree.root)

    print("-----------------------")
    print("Postorder Traversal")
    tree.postorder_traversal(tree.root)

    print("-----------------------")
    print(tree.height(tree.root))

    print("-----------------------")
    print(tree.diameter(tree.root))

    print("-----------------------")
    bst = BinarySearchTree(10)
    values=[5,15,2,5,13,22,1,14]
    for v in values:
        bst.insert(v)
    bst.printTree(bst.root)
    print(bst.searchClosest(12))
main()
