class HeapPriorityQueue:
    def __init__(self):
        # Initialize an empty priority queue backed by a heap
        self._data = []

    def upheap(self, j):
        # Perform up-heap bubbling to maintain the heap order property after adding an element
        if j > 0:
            parent = (j - 1) // 2
            if self._data[j] < self._data[parent]:
                # Swap the element with its parent if it violates the heap order property
                self._data[j], self._data[parent] = self._data[parent], self._data[j]
                # Recursively upheap to continue maintaining the heap order property
                self.upheap(parent)

    def add(self, key, value):
        # Add a new key-value pair to the priority queue
        self._data.append((key, value))
        # Perform up-heap bubbling to maintain the heap order property
        self.upheap(len(self._data) - 1)

    def __str__(self):
        # Return a string representation of the priority queue showing only the keys
        return str([item[0] for item in self._data])


# Example usage
pq = HeapPriorityQueue()
pq.add(5, 'apple')
pq.add(9, 'banana')
pq.add(3, 'orange')
pq.add(7, 'grape')
pq.add(1, 'kiwi')

print("Heap after adding elements:")
print(pq)

pq.add(4, 'pear')

print("\nHeap after adding 'pear':")
print(pq)
