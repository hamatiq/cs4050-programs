import numpy as np
def LCS_length(x,y):
    m = len(x)
    n = len(y)
    b = np.zeros(shape = (m,n), dtype=str)
    c = np.zeros(shape = (m+1,n+1), dtype=int)
    # for i in range(1,m):
    #     c[i,0] = 0
    # for j in range(0,n):
    #     c[0,j] = 0
    for i in range (1,m+1):
        for j in range(1,n+1):
            if (x[i-1] == y[j-1]):
                c[i,j]=c[i-1,j-1]+1
                b[i-1,j-1] = "D"
            elif (c[i-1,j] >= c[i,j-1]):
                c[i,j]= c[i-1,j]
                b[i-1,j-1]= "U"
            else:
                c[i,j] = c[i,j-1]
                b[i-1,j-1] = "L"
    return (c,b)


def Print_LCS(b,x,i,j):
    if i == 0 or j == 0:
        return
    if b[i,j] == 'D':
        Print_LCS(b,x,i-1,j-1)
        print (x[i])
    elif b[i,j] == 'U':
        Print_LCS(b,x,i-1,j)
    else:
        Print_LCS(b,x,i,j-1)

x = "01101"
y = "110101"

lcs = LCS_length(x,y)
Print_LCS(lcs[1],x,len(x)-1,len(y)-1)

print (lcs[0])
print (lcs[1])