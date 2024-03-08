class PositionalList:
    class Position:
        def __init__(self, container, element, prev=None, next=None):
            # Constructor for the Position class
            self.container = container  # Reference to the PositionalList containing this position
            self.element = element  # The element stored in this position
            self.prev = prev  # Reference to the previous position in the list
            self.next = next  # Reference to the next position in the list

        def __eq__(self, other):
            # Override the equality comparison for positions
            return type(other) is type(self) and other.container is self.container and other.element == self.element

    def __init__(self):
        # Constructor for the PositionalList class
        self.header = self.Position(self, None)  # Sentinel node at the beginning
        self.trailer = self.Position(self, None)  # Sentinel node at the end
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0  # Number of elements in the list

    def __len__(self):
        # Return the number of elements in the list
        return self.size

    def is_empty(self):
        # Check if the list is empty
        return self.size == 0

    def first(self):
        # Return the first position in the list
        if self.is_empty():
            raise ValueError("List is empty")
        return self.header.next

    def last(self):
        # Return the last position in the list
        if self.is_empty():
            raise ValueError("List is empty")
        return self.trailer.prev

    def before(self, p):
        # Return the position before the given position p
        if p.container is not self:
            raise ValueError("Position does not belong to this list")
        return p.prev

    def after(self, p):
        # Return the position after the given position p
        if p.container is not self:
            raise ValueError("Position does not belong to this list")
        return p.next

    def __iter__(self):
        # Iterate over the positions in the list
        cursor = self.first()
        while cursor is not self.trailer:
            yield cursor
            cursor = self.after(cursor)

    def add_between(self, e, predecessor, successor):
        # Add a new position with element e between two existing positions
        new_position = self.Position(self, e, predecessor, successor)
        predecessor.next = new_position
        successor.prev = new_position
        self.size += 1
        return new_position

    def add_first(self, e):
        # Add a new position with element e at the beginning of the list
        return self.add_between(e, self.header, self.header.next)

    def add_last(self, e):
        # Add a new position with element e at the end of the list
        return self.add_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
        # Add a new position with element e before the given position p
        predecessor = self.before(p)
        return self.add_between(e, predecessor, p)

    def add_after(self, p, e):
        # Add a new position with element e after the given position p
        successor = self.after(p)
        return self.add_between(e, p, successor)

    def delete(self, p):
        # Remove and return the element at position p
        if self.is_empty():
            raise ValueError("List is empty")
        predecessor = self.before(p)
        successor = self.after(p)
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = p.element
        p.container = p.prev = p.next = None  # Help garbage collection
        return element

    def replace(self, p, e):
        # Replace the element at position p with a new element e
        old_element = p.element
        p.element = e
        return old_element

    def indexOf(self, p):
        # Find and return the index of the given position p in the list
        index = 0
        for position in self:
            if position == p:
                return index
            index += 1
        raise ValueError("Position not found in the list")

# Testing the indexOf method
if __name__ == "__main__":
    my_list = PositionalList()
    positions = []

    for i in range(5):
        positions.append(my_list.add_last(i))

    # Test the indexOf method
    for pos in positions:
        index = my_list.indexOf(pos)
        print(f"Index of position {pos.element} is {index}")
