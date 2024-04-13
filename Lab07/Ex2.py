class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def merge(queue1, queue2):
    merged_queue = Queue()

    while not queue1.is_empty() and not queue2.is_empty():
        if queue1.items[0] < queue2.items[0]:
            merged_queue.enqueue(queue1.dequeue())
        else:
            merged_queue.enqueue(queue2.dequeue())

    while not queue1.is_empty():
        merged_queue.enqueue(queue1.dequeue())

    while not queue2.is_empty():
        merged_queue.enqueue(queue2.dequeue())

    return merged_queue


def bottom_up_merge_sort(items):
    queues = [Queue() for _ in range(len(items))]
    for i, item in enumerate(items):
        queues[i].enqueue(item)

    while len(queues) > 1:
        merged_queues = []
        for i in range(0, len(queues), 2):
            if i + 1 < len(queues):
                merged_queue = merge(queues[i], queues[i + 1])
                merged_queues.append(merged_queue)
            else:
                merged_queues.append(queues[i])
        queues = merged_queues

    sorted_items = []
    while not queues[0].is_empty():
        sorted_items.append(queues[0].dequeue())
    return sorted_items


# Test the implementation
if __name__ == "__main__":
    items = [4, 2, 7, 1, 9, 5, 3, 8, 6]

    # Print unsorted items
    print("Unsorted items:", items)

    # Sort the items and print the sorted list
    sorted_items = bottom_up_merge_sort(items)
    print("Sorted items:", sorted_items)
