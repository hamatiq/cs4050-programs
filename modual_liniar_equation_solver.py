def euclid(a,b,l):
    if (b == 0):
        l.append([a,b,"-"])
        return (a,1,0)
    else:
        l.append([a,b,(a//b)])
        i = len(l)+1
        prime = euclid(b,a%b,l)
        dxy = (prime[0],prime[2],prime[1]-(a//b)*prime[2])
        l[i-1].append(prime[0])
        l[i-1].append(prime[1])
        l[i-1].append(prime[2])
        i -=1
        return (dxy)

def mod_lin_equ_solver(a,b,n):
    l=[]
    dxy=euclid(n,a,l)
    l[0].append(dxy[0])
    l[0].append(dxy[1])
    l[0].append(dxy[2])
    for i in l:
        print (i)
    dyx = dxy
    d = dyx[0]
    y = dyx[1]
    x = dyx[2]
    solution = []
    if ( b % d == 0):
        x0 = (x*(b/d))%n
        # x0 = int(x0)
        # print(x0)
        for i in range (d):
            s = (x0+(i*(n/d)))
            solution.append(s%n)
        return (solution)
    else:
        print("no solution")

#solving ax=b(mod n)
a = 1
b = 220
n = 63

if (a<n):
    mles = mod_lin_equ_solver(a,b,n)
else:
    mles = mod_lin_equ_solver(n,b,a)
print (mles)