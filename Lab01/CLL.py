class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def clone(self):
        if not self.head:
            return CircularlyLinkedList()

        new_list = CircularlyLinkedList()
        current = self.head
        while True:
            new_list.append(current.data)
            current = current.next
            if current == self.head:
                break

        return new_list

def main():
    # Example usage
    original_list = CircularlyLinkedList()
    for i in range(1, 6):
        original_list.append(i)

    print("Original list:")
    original_list.display()

    cloned_list = original_list.clone()

    print("\nCloned list:")
    cloned_list.display()

if __name__ == "__main__":
    main()
