def sort_by_count(a):
    n = len(a)
    count = [0]*n
    s = [0]*n
    
    # Counting the number of elements smaller than or equal to each element
    for i in range(n):
        for j in range(n):
            if a[i]>a[j]:
                count[i] += 1
            elif a[i] == a[j] and i > j:
                count[i] += 1

    for i in range(n):
        s[count[i]] = a[i]

    return s


a = [13, 46, 24, 52, 20, 9, 52, 13]
s = sort_by_count(a)
print(s)

#Complexity : O(n²)