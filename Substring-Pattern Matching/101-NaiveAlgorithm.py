def naive_string_matching(text,pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(0,n-m+1):
        j = 0
        
        while j < m and pattern[j]==text[i+j]:
            j+=1
            
        if j==m:
            return i
            
    return -1
    
text = "abcaabbacb"

pattern = "acb"

print(naive_string_matching(text,pattern))