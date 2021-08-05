class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node_before = self.get_node(position - 1)
            new_node.next = node_before.next
            node_before.next = new_node
        self.size += 1

    def drop(self, position):
        if position == 0:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
        else:
            previous_node = self.get_node(position - 1)
            removed_node = previous_node.next
            previous_node.next = removed_node.next
            removed_node.next = None
        self.size -= 1
        return removed_node

    def get_node(self, position):
        if position < 0 or position > self.size:
            raise Exception("No such index")
        current = self.head
        for i in range(0, position):
            current = current.next
        return current

    def print(self):
        current = self.head
        for i in range(0, self.size):
            print("{} : {}".format(i, current.data))
            current = current.next


def main():
    linked_list = LinkedList()
    linked_list.insert(0, "Leandro")
    linked_list.insert(0, "Karen")
    linked_list.insert(0, "Izabel")
    linked_list.insert(0, "Marines")
    linked_list.insert(0, "Leticia")
    linked_list.insert(0, "Karina")
    linked_list.insert(0, "Keivin")
    linked_list.insert(0, "Joel")
    linked_list.insert(3, "Position 3")
    linked_list.insert(6, "Position 6")

    linked_list.drop(3)
    linked_list.drop(5)  # Was position 6 before above removal

    linked_list.print()
    print(linked_list.get_node(7).data)

main()
