def Rabin_Karp(text, pattern):
    d = 10         
    q = 13          
    m = len(pattern)  
    n = len(text)     
    p = 0          
    t = 0           
    h = 1 
    
    for i in range(m - 1):
        h = (h * d) % q
        
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        
    for i in range(n - m + 1):
        j = 0
        if p == t:
            while j < m:
                if text[i + j] != pattern[j]:
                    break
                j += 1
        
        if j == m:
            print("Pattern is found at position: " + str(i))
            
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            
            if t < 0:
                t = t + q

text = "abcaabbacb"
pattern = "acb"

Rabin_Karp(text, pattern)