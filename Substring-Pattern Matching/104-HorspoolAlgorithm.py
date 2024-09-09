def shift_table(P):
    Table = {}
    m = len(P)
    for j in range(0,m-1):
        Table[P[j]] = m-1-j

    return Table    

def Harspool_algo(P,T):
    m = len(P)
    n = len(T)

    i = m
    Table = shift_table(P)
    print(Table)

    while i <= n-1:
        k = 0

        while k<=m-1 and P[m-1-k]==T[i-k]:
            k = k+1
        
        if k==m:
            return i-m+1
        else:
            if T[i] in Table:
                i+=Table[T[i]]
            else:
                i+=m

    return -1

T = "Jimy Hailed The Leader To Stop"
P = "Leader"

print(Harspool_algo(P,T))