a = [99, 45, 23, 65, 16, 83, 56, 86, 55, 23, 654, 786, 108, 100]
target = 108
flag = 0
for i in range(len(a)):
    if a[i]==target:
        print(f'{target} found at index {i}')
        flag = 1

if flag==0:
    print(f'{target} not in the sequence!')

#Complexity : O(n)