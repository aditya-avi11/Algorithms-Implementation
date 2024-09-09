def LPS(pattern):
    M = len(pattern)
    lps = [0]*M
    length = 0
    i = 1
    
    while i < M:
        if pattern[i]==pattern[length]:
            length+=1 
            lps[i]=length
            
            i+=1
            
        else:
            if length!=0:
                length = lps[length-1]
                
            else:
                lps[i]=0
                i+=1 
        
    return lps
    
def KMP_Search(text,pattern):
    N = len(text)
    M = len(pattern)
    lps = LPS(pattern)
    i = 0
    j = 0
    
    while i < N:
        if pattern[j]==text[i]:
            i+=1
            j+=1
        if j==M:
            print(f"Found at pattern at index {i-j}")
            j = lps[j-1]
        
        elif i<N and pattern[j]!=text[i]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
                
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"



KMP_Search(text,pattern)