def isBeautifulNumber(n):
    n = str(n)
    x = n
    x = x[::-1]
    if (x!=n): return False
    if(len(n)%2==1): return False
    for i in n: 
        if (i!='0' and i!='2' and i!='4' and i!='6' and i!='8'): return False
    return True
T = int(input())
for i in range(T):
    n = int(input())
    for x in range(22,n):
        if(isBeautifulNumber(x)):print(x,end=" ")
    print()    
