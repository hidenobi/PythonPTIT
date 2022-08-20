import math


[n,k]=map(int,input().split())
a=10**(k-1)
b=10**k
c=0
for i in range(a,b):
    if math.gcd(n,i)==1:
        c+=1
        if(c==10):
            c=0
            print(i)
        else:
            print(i,end=" ")    