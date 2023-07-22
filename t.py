# 1
from itertools import groupby
from functools import reduce

def max_multiplication(s):
    if not isinstance(s, str):
        return None
        
    groups = groupby(s, key=str.isdigit)

    digit_chunks = [''.join(g) for k, g in groups if k] # ['12345']
    if len(digit_chunks)==1:
        return reduce(lambda x, y: int(x) * int(y), digit_chunks[0]) # 120

    int_chunks = [sorted(map(int, list(i)))[-4:] for i in digit_chunks if len(i)>=4]
    if len(int_chunks)==0:
        return None
    return reduce(lambda x, y: x * y, max(int_chunks, key=lambda x: sum(x)))

# Test cases
print(max_multiplication('abc12345def'))  # Output: 120
print(max_multiplication('a1b2c3d4e'))    # Output: None


# 2
def count_ones_in_binary(s):
    # Count the number of '1's in the binary representation of s
    return bin(s).count('1')

def binary_sort(arr):
    # Sort the array based on the number of '1's in binary and then by decimal value
    return sorted(arr, key=lambda x: (count_ones_in_binary(x), x))

# Test case
result = binary_sort([3, 7, 8, 9])
print(result)  # Output: [8, 3, 9, 7]
