def multiply(m, n):
    # Base case: if either m or n is 0, the product is 0
    if m == 0 or n == 0:
        return 0
    
    # Recursive case: add m to the product of (m-1) and n
    # or add n to the product of m and (n-1)
    return m + multiply(m, n - 1)

# Example usage:
m = 5
n = 3
result = multiply(m, n)
print(f'The product of {m} and {n} is: {result}')
