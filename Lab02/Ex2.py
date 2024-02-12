#Libraries
import numpy as np
import matplotlib.pyplot as plt
import time

# Function to calculate prefix averages with a less optimized approach
def calculate_prefix_average1(array):
    n = len(array)
    prefix_avg = []

    # Iterate through the array
    for i in range(n):
        # Calculate the total sum of the subarray up to index i
        total = sum(array[:i+1])
        # Append the prefix average to the list
        prefix_avg.append(total / (i + 1))

    return prefix_avg

# Function to calculate prefix averages with a more optimized approach
def calculate_prefix_average2(array):
    n = len(array)
    prefix_avg = []
    total = 0

    # Iterate through the array
    for i in range(n):
        # Update the running total
        total += array[i]
        # Append the prefix average to the list
        prefix_avg.append(total / (i + 1))

    return prefix_avg

# Function to measure the runtime of a given function with a specific array
def measure_runtime(func, array):
    start_time = time.time()
    # Call the provided function with the array
    func(array)
    end_time = time.time()
    # Return the elapsed time
    return end_time - start_time

# Function to evaluate the runtime performance of a given function and plot the results
def evaluate_and_plot(func_name, epoch, initial=10):
    elapse_times = []

    # Iterate through the specified number of epochs
    for test in range(1, epoch+1):
        # Generate an array of increasing size
        array_size = 100 * test * initial
        array = list(np.random.randint(101, size=array_size))

        # Measure the runtime of the given function for the current array
        runtime = measure_runtime(func_name, array)
        elapse_times.append(runtime)

        # Print array size and elapsed time for each iteration
        print(f'Array size: {array_size}\tElapsed time: {runtime}')

    return elapse_times

# Evaluate and plot results for the less optimized algorithm
elapse_times1 = evaluate_and_plot(calculate_prefix_average1, 10)

# Evaluate and plot results for the more optimized algorithm
elapse_times2 = evaluate_and_plot(calculate_prefix_average2, 10)

# Create a range of epochs for the x-axis of the plot
epochs = range(1, 11)

# Plot the results for both algorithms
plt.plot(epochs, elapse_times1, color='green', linewidth=2.5, linestyle='-', label='calculate_prefix_average1')
plt.plot(epochs, elapse_times2, color='purple', linewidth=2.0, linestyle=':', label='calculate_prefix_average2')

# Add labels and legend to the plot
plt.title('Analysis of Prefix Averages')
plt.xlabel('Epoch')
plt.ylabel('Runtime')
plt.legend()

# Display the plot
plt.show()
