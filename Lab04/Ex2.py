# Define a simple Stack class with basic operations
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top element from the stack if it's not empty
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        # Return the top element of the stack without removing it if the stack is not empty
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)

def transfer(source_stack, target_stack):
    # Transfer elements from the source stack to the target stack
    while not source_stack.is_empty():
        # Remove an element from the top of the source stack
        item = source_stack.pop()
        # Add the removed element to the top of the target stack
        target_stack.push(item)

# Test the transfer method
stack_S = Stack()
stack_T = Stack()

# Push some elements onto stack S
stack_S.push(1)
stack_S.push(2)
stack_S.push(3)
stack_S.push(4)

# Display the state of stacks before the transfer
print("Stack S before transfer:", stack_S.items)
print("Stack T before transfer:", stack_T.items)

# Transfer elements from stack S to stack T
transfer(stack_S, stack_T)

# Display the state of stacks after the transfer
print("Stack S after transfer:", stack_S.items)
print("Stack T after transfer:", stack_T.items)
