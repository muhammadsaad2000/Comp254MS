class MyNode:
    def __init__(self, key, val, prev=None, next=None):
        # Initialize a node with key, value, previous, and next pointers
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head and tail sentinel nodes
        self.head = MyNode(None, 'head')
        self.tail = MyNode(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
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

    def delete(self, node):
        # Delete a node from the linked list
        prev = node.prev
        next_node = node.next
        next_node.prev = prev
        prev.next = next_node
        self.size -= 1

    def get_list(self):
        # Get a list of nodes in the linked list
        ret = []
        current = self.head.next
        while current != self.tail:
            ret.append(current)
            current = current.next
        return ret

    def get_by_key(self, key):
        # Get a node by its key from the linked list
        current = self.head.next
        while current != self.tail:
            if current.key == key:
                return current
            current = current.next
        return None

class MyMap:
    def __init__(self, capacity=16, load_factor=5):
        # Initialize a map with a certain capacity and load factor
        self.capacity = capacity
        self.load_factor = load_factor
        self.buckets = [MyLinkedList() for _ in range(capacity)]

    def reset(self):
        # Reset the map, to be implemented by subclasses
        pass

    def hash_function(self, key):
        # Hash function to determine bucket index
        return hash(key) % self.capacity

    def put(self, key, val):
        # Put a key-value pair into the map, to be implemented by subclasses
        pass

    def get(self, key):
        # Get the value associated with a key, to be implemented by subclasses
        pass

    def delete(self, key):
        # Delete a key-value pair from the map, to be implemented by subclasses
        pass

class HashMap(MyMap):
    def reset(self):
        # Reset the hashmap by doubling the capacity and rehashing elements
        new_buckets = [MyLinkedList() for _ in range(self.capacity * 2)]
        old_buckets = self.buckets
        self.capacity *= 2
        for bucket in old_buckets:
            nodes = bucket.get_list()
            for node in nodes:
                hash_key = self.hash_function(node.key)
                new_buckets[hash_key].append(node)
        self.buckets = new_buckets

    def put(self, key, val):
        # Put a key-value pair into the hashmap, resize if necessary
        hash_key = self.hash_function(key)
        bucket = self.buckets[hash_key]
        if bucket.size >= self.load_factor * self.capacity:
            self.reset()
            hash_key = self.hash_function(key)
            bucket = self.buckets[hash_key]
        bucket.append(MyNode(key, val))

    def get(self, key):
        # Get the value associated with a key from the hashmap
        hash_key = self.hash_function(key)
        bucket = self.buckets[hash_key]
        node = bucket.get_by_key(key)
        if node:
            return [bucket, node]
        else:
            # If key not found in the current bucket, search in subsequent buckets
            for i in range(hash_key + 1, self.capacity):
                bucket = self.buckets[i]
                node = bucket.get_by_key(key)
                if node:
                    return [bucket, node]
            return None

    def delete(self, key):
        # Delete a key-value pair from the hashmap
        result = self.get(key)
        if result:
            bucket, node = result
            bucket.delete(node)
            return True
        return False


# Example usage:
my_hash_map = HashMap(capacity=2, load_factor=2)
my_hash_map.put(1, 9)
my_hash_map.put(1, 5)
my_hash_map.put(1, 4)
my_hash_map.put(1, 7)
my_hash_map.put(1, 1)
for bucket in my_hash_map.buckets:
    nodes = bucket.get_list()
    for node in nodes:
        print('key is %s, value is %s' % (str(node.key), str(node.val)))
