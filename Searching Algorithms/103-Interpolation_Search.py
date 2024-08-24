def getpos(a,x,l,h):
    # Guard against division by zero
    if a[h] == a[l]:
        return l
    # Calculate the position using the interpolation formula
    pos = l + ((x - a[l]) * (h - l)) // (a[h] - a[l])
    return pos

def interpolation_search(a, x, l, h):
    while l <= h and x >= a[l] and x <= a[h]:
        # Call getpos to find the position
        pos = getpos(a, x, l, h)
        
        # If the element is found
        if a[pos] == x:
            return pos
        
        # If x is larger, x is in the upper part
        if a[pos] < x:
            l = pos + 1
        # If x is smaller, x is in the lower part
        else:
            h = pos - 1

    # If the element was not found
    return -1


a = [9, 13, 13, 20, 24, 46, 52, 52] #array must be sorted for interpolatoin search
x = 46
pos = interpolation_search(a,x,0,len(a)-1)
if pos!=-1:
    print(f'{x} found at index {pos}')
else:
    print(f'{x} not found in the array')

#Complexity : Best, Average Case: O(log•log n), Worst Case : O(n)