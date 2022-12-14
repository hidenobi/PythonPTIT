MOD = 10**9+7
T = int(input())
for t in range(T):
    n,k = map(int,input().split())
    a = [0]
    i = 1
    a.append(i)
    while len(a)<=k:
        i = i*n
        b = list(map(lambda x:(x+i)%MOD,a))
        a+=b
        a = list(set(a))
    sorted(a)
    print(a[k])