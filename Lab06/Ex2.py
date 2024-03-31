class Node:
    def __init__(self, key, val, prev=None, next=None):
        # Initialize a node with key, value, previous, and next pointers
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head and tail sentinel nodes
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append_node(self, node):
        # Append a node to the end of the linked list
        prev = self.tail.prev
        node.prev = prev
        node.next = prev.next
        prev.next = node
        node.next.prev = node
        self.size += 1

    def is_empty(self):
        # Check if the linked list is empty
        return self.size == 0

    def remove_node(self, node):
        # Remove a node from the linked list
        prev = node.prev
        next_node = node.next
        next_node.prev = prev
        prev.next = next_node
        self.size -= 1

    def get_nodes(self):
        # Get a list of nodes in the linked list
        nodes = []
        current = self.head.next
        while current != self.tail:
            nodes.append(current)
            current = current.next
        return nodes

    def get_node_by_key(self, key):
        # Get a node by its key from the linked list
        current = self.head.next
        while current != self.tail:
            if current.key == key:
                return current
            current = current.next
        return None

class HashMap:
    def __init__(self, capacity=16, load_factor=5):
        # Initialize a hashmap with a certain capacity and load factor
        self.capacity = capacity
        self.load_factor = load_factor
        self.buckets = [LinkedList() for _ in range(capacity)]

    def reset_capacity(self):
        # Reset the capacity of the hashmap by doubling the number of buckets
        pass

    def hash_function(self, key):
        # Hash function to determine the index of a key in the hashmap
        return hash(key) % self.capacity

    def put_value(self, key, val):
        # Put a key-value pair into the hashmap
        pass

    def get_value(self, key):
        # Get the value associated with a key from the hashmap
        pass

    def remove_key(self, key):
        # Remove a key-value pair from the hashmap
        pass

class SortedMap(HashMap):
    def reset_capacity(self):
        # Reset the capacity of the sorted map by doubling the number of buckets and rehashing elements
        new_buckets = [LinkedList() for _ in range(self.capacity * 2)]
        prev_capacity = self.capacity
        self.capacity = self.capacity * 2
        for i in range(prev_capacity):
            bucket = self.buckets[i]
            nodes = bucket.get_nodes()
            for node in nodes:
                new_index = node.key % self.capacity
                new_bucket = new_buckets[new_index]
                new_bucket.append_node(node)
        self.buckets = new_buckets

    def put_value(self, key, val):
        # Put a key-value pair into the sorted map, resize if necessary
        if key >= self.capacity:
            self.reset_capacity()
        bucket = self.buckets[key]
        if bucket.size >= self.load_factor * self.capacity:
            self.reset_capacity()
        bucket = self.buckets[key]
        bucket.append_node(Node(key, val))

    def get_value(self, key):
        # Get the value associated with a key from the sorted map
        if key < 0 or key >= self.capacity:
            return 'Key not found'
        bucket = self.buckets[key]
        node = bucket.get_node_by_key(key)
        return node.val if node else 'No value'

    def remove_key(self, key):
        # Remove a key-value pair from the sorted map
        node_val = self.get_value(key)
        if node_val is None:
            return False
        bucket = self.buckets[key]
        node = bucket.get_node_by_key(key)
        bucket.remove_node(node)
        return True

# Example usage:
my_sorted_map = SortedMap(capacity=2, load_factor=2)
my_sorted_map.put_value(1, 5)
my_sorted_map.put_value(3, 6)
my_sorted_map.put_value(2, 9)
my_sorted_map.put_value(5, 7)
my_sorted_map.put_value(4, 0)

# Print nodes in each bucket
for bucket in my_sorted_map.buckets:
    nodes = bucket.get_nodes()
    for n in nodes:
        print('Key:', n.key, 'Value:', n.val)

# Test get_value method
print(my_sorted_map.get_value(2))  # Output: 9
print(my_sorted_map.get_value(0))  # Output: Key not found
print(my_sorted_map.get_value(10)) # Output: Key not found
