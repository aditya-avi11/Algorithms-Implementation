def distributed_counting_sort(a):
    l = min(a)  # Use min(a) to get the lower bound
    u = max(a)  # Use max(a) to get the upper bound
    n = len(a)
    range_size = u - l + 1
    
    d = [0] * range_size  # Correctly initialize the counting array
    s = [0] * n  # Initialize the sorted array
    
    # Count occurrences of each element
    for i in range(n):
        d[a[i] - l] += 1
    
    # Compute the cumulative sum to get positions
    for j in range(1, range_size):
        d[j] += d[j - 1]
    
    # Build the sorted array
    for i in range(n - 1, -1, -1):  # Correct the range to include 0
        j = a[i] - l
        s[d[j] - 1] = a[i]
        d[j] -= 1
    
    return s

a = [13, 46, 24, 52, 20, 9, 52, 13]
s = distributed_counting_sort(a)
print(s)

#Complexity : O(n)