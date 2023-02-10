def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def multi_group(n):
    z=[]
    for a in range(1,n):
        if (gcd(a,n) == 1):
            z.append(a)
    return (z)

def multiplicative_group_table(n):
    table = []
    group = multi_group(n)
    for a in group:
        x = [e*a for e in group]
        table.append(x)
    
    for a in range(len(table)):
        table[a] = [e%n for e in table[a]]
    return table

def addative_group_table(n):
    table = []
    group = [e for e in range(n)]
    for a in group:
        x = [e+a for e in group]
        table.append(x)
    
    for a in range(len(table)):
        table[a] = [e%n for e in table[a]]
    return table

print (multi_group(21))
# table =addative_group_table(6)
# for t in table:
#     print (t)
# print(addative_group_table(6))