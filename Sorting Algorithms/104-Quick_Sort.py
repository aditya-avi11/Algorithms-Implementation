# Quick Sort: "Partitions the array around a pivot, placing smaller elements 
#  before and larger elements after, then recursively sorts the partitions."

def partition(l,h):
    pivot = a[l]
    i = l
    j = h
    while i<j:
        #increment i until you find an element greater than pivot
        while i < h and a[i]<=pivot:
            i += 1
        #decrement j until you find an element smaller than pivot
        while j > l and a[j]>pivot:
            j -= 1
        
        if i<j:
            # Swap elements at i and j
            a[i], a[j] = a[j], a[i]

    # Swap pivot with element at j
    a[l], a[j] = a[j], a[l]

    return j    

def quick_sort(l,h):
    if l<h:
        j = partition(l,h)
        quick_sort(l,j-1)
        quick_sort(j+1,h)

a = [13, 46, 24, 52, 20, 9]
quick_sort(0, len(a) - 1)
print(a)

#Complexity : Best Case : O(n•log n), Worst Case : O(n²)