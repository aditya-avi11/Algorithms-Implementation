#Merge Sort: "Recursively divides the array into halves, then merges them back in sorted order."

#function for comparing and merging
def merge(b,c,a):
    i=0
    j=0
    k=0
    p = len(b)
    q = len(c)
    while i<p and j<q:
        if b[i]<=c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    # Copy remaining elements from b, if any
    while i < p:
        a[k] = b[i]
        i += 1
        k += 1

    # Copy remaining elements from c, if any
    while j < q:
        a[k] = c[j]
        j += 1
        k += 1

#recursive function for splitting and merging
def mergeSort(a, n):
    if n>1:
        b = a[0:(n//2)]
        c = a[n//2:n]
        mergeSort(b, len(b))
        mergeSort(c, len(c))
        merge(b,c,a)

a = [13,46,24,52,20,9]
mergeSort(a, len(a))
print(a)

#Complexity : O(n•log n) [for all, best, average and worst case]