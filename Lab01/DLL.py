class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.tail = new_node

    def concatenate(self, other):
        if other.head:
            if not self.head:
                self.head = other.head
            else:
                self.tail.next = other.head
                other.head.prev = self.tail
            self.tail = other.tail

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    # Example usage
    L = DoublyLinkedList()
    L.append(1)

    M = DoublyLinkedList()
    M.append(2)
    M.append(3)

    print("List L before concatenation:")
    L.print_list()

    print("\nList M before concatenation:")
    M.print_list()

    L.concatenate(M)

    print("\nList L after concatenation:")
    L.print_list()

if __name__ == "__main__":
    main()
