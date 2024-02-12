def example1(arr):
    n = len(arr)  # length of input array 
    total = 0     # Initialize variable
    for j in range(n):  # Iterate through index 'j' from 0 to n-1
        total += arr[j]  # Add the element at index 'j' to the 'total'
    return total  

# Example usage
arr = [1, 2, 3, 4, 5]  # Create array with  1, 2, 3, 4, 5
result = example1(arr)  # Call example1 
print(result)  
# the time complexity of the method is O(n) because the algorithm has a linear relationship with the size of the input array.  # Print the result, which should be 15

def example2(arr):
    n = len(arr)      # length of input array 
    total = 0         # Initialize variable
    for j in range(0, n, 2):  # Iterate even index 'j' from 0 to n-1 with a step size of 2
        total += arr[j]  # Add  element at even index 'j' to the 'total'
    return total  

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]  # Create elements 1, 2, 3, 4, 5, 6, 7, 8
result = example2(arr)  # Call example2
print(result)  
# takes an array, iterates and calculates the sum of elements at even indices. Prints the sum of elements at even indices (1 + 3 + 5 + 7 = 16).


def example3(arr):
    n = len(arr)      # length of input array 
    total = 0         # Initialize variable
    for j in range(n):          # Outer loop: Iterate index 'j' from 0 to n-1
        for k in range(j + 1):   # Inner loop: Iterate index 'k' from 0 to j
            total += arr[j]      # Add the element at index 'j' to the 'total' for each iteration of the inner loop
    return total   

# Example usage
arr = [1, 2, 3, 4]  # Create array 1, 2, 3, 4
result = example3(arr)  # Call example3
print(result)  
# the result is calculated as follows: 1 + (2 + 2) + (3 + 3 + 3) + (4 + 4 + 4 + 4) = 30.


def example4(arr):
    n = len(arr)      # length of input array 
    prefix = 0        # Initialize prefix to store prefix sum
    total = 0         # Initialize total to store the sum of prefix sums
    for j in range(n):          # Loop from 0 to n-1
        prefix += arr[j]         # Add element at index j to prefix
        total += prefix          # Add the current prefix' to total
    return total  

# Example usage
arr = [1, 2, 3, 4]  # Create array 1, 2, 3, 4
result = example4(arr)  # Call example4
print(result)  
# In this example, the result is calculated as follows: 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) = 20.

def example5(first, second):
    n = len(first)     # length of arrays first and second
    count = 0          # Initialize count to store the number of occurrences
    for i in range(n):             # Outer loop: Iterate through i from 0 to n-1
        total = 0                   # Initialize total to store the sum of elements from first
        for j in range(n):         # Middle loop: Iterate index j from 0 to n-1
            for k in range(j + 1):  # Inner loop: Iterate k from 0 to j
                total += first[k]    # Add elements to k from first to the total
        if second[i] == total:      # Check if the current element in second is equal to the calculated total
            count += 1               # If true, increment 
    return count  # 

# Example usage
first_array = [1, 2, 3, 4]        # Create array 1, 2, 3, 4
second_array = [10, 5, 14, 22]    # Create array 10, 5, 14, 22
result = example5(first_array, second_array)  # Call example5 
print(result)  # Print the count of occurrences satisfying the condition

