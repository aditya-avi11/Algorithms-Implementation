#Binary Search Iterative Approach
def binary_search_iterative(arr, target, l, h):
    while l<=h:
        mid = (l+h)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            l = mid+1
        else:
            h = mid-1

    # Target is not present in the array
    return -1       


#Binary Search Recursive Approach
def binary_search_recursive(arr, target, l, h):
    if l>h:
        return -1
    else:
        mid = (l+h)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            return binary_search_recursive(arr, target, mid+1, h)
        else:
            return binary_search_recursive(arr, target, l, mid-1)
        

arr = [33,44,55,66,77,88,99,100,110,120,125,145]
l = 0
h = len(arr)
target = 110

result = binary_search_recursive(arr,target,l,h)
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the array")

#Complexity : Best Case:O(1) [When element is at mid], Average & Worst Case : O(log n)