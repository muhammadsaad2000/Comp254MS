import numpy as np
import time

def is_unique1(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return False
    return True

def is_unique2(arr):
    n = len(arr)
    arr.sort()
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            return False
    return True

def find_largest_size(func_name, min_size, max_size, time_limit=60):
    size = (min_size + max_size) // 2
    arr = list(np.random.randint(101, size=size))

    if size < max_size and min_size != max_size:
        start = time.time()

        if func_name == 'is_unique1':
            is_unique1(arr)
        elif func_name == 'is_unique2':
            is_unique2(arr)
        else:
            print('Invalid function name')
            return

        end = time.time()
        elapsed_time = end - start

        print(f'Array size: {size}\tElapsed time: {elapsed_time}')

        if abs(elapsed_time - time_limit) < 0.001:
            del arr
            return size
        elif elapsed_time < time_limit:
            del arr
            return find_largest_size(func_name, size + 1, max_size, time_limit)
        elif elapsed_time > time_limit:
            del arr
            return find_largest_size(func_name, min_size, size - 1, time_limit)

    return size

size1 = find_largest_size('is_unique1', 0, 100000000, 1)
size2 = find_largest_size('is_unique2', 0, 10000000000, 1)
