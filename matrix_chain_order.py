#dynamic programming
#matrix chain multiplication
import numpy as np
# global t #t needs to be a global variable so i can write to from a recursive function
# t = ''

# ignore this had some shower clarity i was not returnting the string at every recrsion interval

# un used function to workout matrix multiplication
def matrix_multiply(a,b):
    if a.shape[1] != b.shape[0]:
        return ("incompatable dimentions")
    else:
        c = np.empty(shape=(a.shape[0],b.shape[1]),dtype = int)
        for i in range(a.shape[0]):
            for j in range(b.shape[1]):
                c[i][j] = 0
                for k in range(a.shape[1]):
                    c[i][j] = c[i][j]+a[i][k]*b[k][j]
        return c

# bread and butter
def Matrix_Chain_Order(p):
    n = len(p)-1
    m = np.zeros(shape=(n,n),dtype= int)
    s = np.zeros(shape=(n,n+1),dtype =int)
    for i in range(n):
        m[i][i] = 0
    # print (m)
    for l in range(1,n): # set l to l-2
        for i in (range(0,(n-l))):
            j = i+l
            # if i or j 
            m[i][j] = 1000000 #attepted to use int('inf') or float('inf) it did not work and surprizingly very large numbers cause integer over flow.
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + (p[i]*p[k+1]*p[j+1])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i+1][j+1]=k+1
    return (m,s) #returns a tuple of 2 matracies 

def Print_Optimal_Parens(s,i,j,t):

    if i == j:
        t = str(t) +" A"+str(i)
        return t
    else:
        t = str(t) + "( "
        t = Print_Optimal_Parens(s,i,s[i,j],t)
        t = Print_Optimal_Parens(s,s[i,j]+1,j,t)
        t = str(t) +  " ) "
        return t
    

# the most optimal way to multiply a set fo matrices 
# given an array ex: [2, 4, 3, 5, 4] matrices a1 = 2x4 a2=4x3 a3=3x5 a4=5x4
a = [5,18,55,4,6,8]
p = Matrix_Chain_Order(a)
# print (p[0]) #for debugging
# print(p[1])
# s = p[1]
# i = 1
# j = 4
t = str("")
t = Print_Optimal_Parens(p[1],1,len(a)-1,t)
print (t)


