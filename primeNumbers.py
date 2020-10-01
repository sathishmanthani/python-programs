# Given k integers less than n, get the list of Prime numbers among them efficiently

# Ancient algorithm "Sieve of Erostenes" 

def prime(n1):
    n = max(n1)
    l = [True]*(n+1)
    k = []
    for i in range(2,int(n**0.5)+1):
        for j in range(i*i,n+1,i):
            l[j]=False
    for i,val in enumerate(l):
        if val and i in n1:
            k.append(i)
    return k


k = [1,2,7,9,15,35]
print(prime(k))
