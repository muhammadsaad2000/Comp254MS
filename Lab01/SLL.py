class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def swapNodes(self, node1, node2):
        if node1 == node2 or not node1 or not node2:
            return

        prev1, current1 = None, self.head
        while current1 and current1 != node1:
            prev1, current1 = current1, current1.next

        prev2, current2 = None, self.head
        while current2 and current2 != node2:
            prev2, current2 = current2, current2.next

        if not current1 or not current2:
            return

        temp = current1.next
        current1.next = current2.next
        current2.next = temp

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current1

def main():
    linked_list = SinglyLinkedList()
    for i in range(1, 6):
        linked_list.append(i)

    print("Original list:")
    linked_list.display()

    node_to_swap_1 = linked_list.head.next  # Node with data 2
    node_to_swap_2 = linked_list.head.next.next.next  # Node with data 4

    linked_list.swapNodes(node_to_swap_1, node_to_swap_2)

    print("\nList after swapping nodes:")
    linked_list.display()

if __name__ == "__main__":
    main()
