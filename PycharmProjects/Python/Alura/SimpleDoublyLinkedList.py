class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def insert(self, position, data):
        new_node = Node(data)
        if self.size == 0:  # If list is empty
            self.head = new_node
            self.end = new_node
        elif position == 0:  # If adding to the beginning
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        elif position == self.size:  # If adding to the end
            new_node.previous = self.end
            self.end.next = new_node
            self.end = new_node
        else:
            position_previous = self.get_node(position - 1)
            position_to_replace = position_previous.next
            new_node = Node(data)
            new_node.next = position_to_replace
            new_node.previous = position_previous
            position_previous.next = new_node
            position_to_replace.previous = new_node
        self.size += 1

    def drop(self, position):
        if self.size == 1:  # If removing last element of the list
            self.head = None
            self.end = None
        elif position == 0:  # If removing from the beginning
            removed_node = self.head
            self.head = removed_node.next
            self.head.previous = None
            removed_node.next = None
        elif position == self.size:  # If removing from the end
            removed_node = self.end
            self.end = removed_node.previous
            self.end.Next = None
            removed_node.previous = None
        else:
            removed_node = self.get_node(position)
            previous_position = removed_node.previous
            next_position = removed_node.next
            previous_position.next = next_position
            next_position.previous = previous_position
            removed_node.previous = None
            removed_node.next = None
        self.size -= 1
        return removed_node


    def get_node(self, position):
        if position < 0 or position > self.size:
            raise Exception("No such index")
        half = self.size // 2
        current = None
        if position <= half:  # If position is before the end of the list, start from the beginning of the list
            current = self.head
            for i in range(0, position):
                current = current.next
        else:  # Else, start from the end and move backwards
            current = self.end
            for i in range(position + 1, self.size)[::-1]:
                current = current.previous
        return current

    def print(self):
        current = self.head
        for i in range(0, self.size):

            next_data = ""
            if current.next is None:
                next_data = "None"
            else:
                next_data = current.next.data

            previous_data = ""
            if current.previous is None:
                previous_data = "None"
            else:
                previous_data = current.previous.data

            print("{} : {} (previous: {}, next: {})".format(i, current.data, previous_data, next_data))
            current = current.next


def main():
    linked_list = DoublyLinkedList()
    linked_list.insert(0, "Leandro")
    linked_list.insert(0, "Karen")
    linked_list.insert(0, "Karina")
    linked_list.insert(0, "Thiego")
    linked_list.insert(0, "Carol")
    linked_list.insert(0, "Izabel")
    linked_list.insert(0, "Paula")
    linked_list.print()
    print("-----------")
    linked_list.insert(2, "Position 2")
    linked_list.print()
    print("-----------")
    linked_list.insert(5, "Position 5")
    linked_list.print()
    print("-----------")
    print("Position 2 : {}".format(linked_list.get_node(2).data))
    print("Position 5 : {}".format(linked_list.get_node(5).data))
    print("-----------")
    linked_list.insert(linked_list.size, "Last Position")
    linked_list.print()
    print("-----------")
    linked_list.insert(0, "First Position")
    linked_list.print()
    print("-----------")
    linked_list.drop(0)
    linked_list.print()
    print("-----------")
    linked_list.drop(linked_list.size)
    linked_list.print()
    print("-----------")
    print("Removed from list: {}".format(linked_list.drop(2).data))
    print("Removed from list: {}".format(linked_list.drop(4).data))
    linked_list.print()



main()
