# Node class represents a single node in a linked list.
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# SinglyLinkedList class represents a singly linked list.
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node in the list
        self.tail = None  # Points to the last node in the list

    def is_empty(self):
        return self.head is None  # Checks if the list is empty

    def append(self, data):
        new_node = Node(data)  # Creates a new node with the given data
        if self.is_empty():
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, append the new node to the end and update the tail
            self.tail.next_node = new_node
            self.tail = new_node

# LinkedQueue class represents a queue implemented using a linked list.
class LinkedQueue:
    def __init__(self):
        self.linked_list = SinglyLinkedList()  # Initializes a linked list for the queue

    def is_empty(self):
        return self.linked_list.is_empty()  # Checks if the queue is empty

    def enqueue(self, element):
        self.linked_list.append(element)  # Adds an element to the end of the queue

    def concatenate(self, Q2):
        if not isinstance(Q2, LinkedQueue):
            raise TypeError("Q2 must be an instance of LinkedQueue")

        if not Q2.is_empty():
            if self.is_empty():
                # If the first queue is empty, set its head and tail to the second queue's head and tail
                self.linked_list.head = Q2.linked_list.head
                self.linked_list.tail = Q2.linked_list.tail
            else:
                # If the first queue is not empty, concatenate the second queue to the end of the first queue
                self.linked_list.tail.next_node = Q2.linked_list.head
                self.linked_list.tail = Q2.linked_list.tail

            # Clear the second queue by resetting its head and tail to None
            Q2.linked_list.head = None
            Q2.linked_list.tail = None

# Testing the concatenate method
q1 = LinkedQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q2 = LinkedQueue()
q2.enqueue(4)
q2.enqueue(5)

print("Queue 1 before concatenation:", q1.linked_list.head.data, q1.linked_list.tail.data)
print("Queue 2 before concatenation:", q2.linked_list.head.data, q2.linked_list.tail.data)

q1.concatenate(q2)

print("Queue 1 after concatenation:", q1.linked_list.head.data, q1.linked_list.tail.data)
print("Queue 2 after concatenation:", q2.linked_list.head, q2.linked_list.tail)
