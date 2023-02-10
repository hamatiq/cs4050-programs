import numpy as np

def extended_euclid(a,b,l):
    if (b == 0):
        l.append([a,b,"-"])
        return (a,1,0)
    else:
        l.append([a,b,(a//b)])
        i = len(l)+1
        prime = extended_euclid(b,a%b,l)
        dxy = (prime[0],prime[2],prime[1]-(a//b)*prime[2])
        l[i-1].append(prime[0])
        l[i-1].append(prime[1])
        l[i-1].append(prime[2])
        i -=1
        return (dxy)

def euclid(a,b):
    if (b==0):
        return a
    else:
        return euclid(b,a%b)
l  = []
dxy=extended_euclid(156,66,l)
l[0].append(dxy[0])
l[0].append(dxy[1])
l[0].append(dxy[2])
for i in l:
    print (i)
