T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        i = int(i)
    maxx = max(a)
    pos = a.index(maxx)
    b = a[:pos:]
    c = a[pos::]
    b.append(m)
    b+=c
    u = []
    v = []
    k = []
    for i in b:
        if i<0:
            u.append(i)
        else:
            k.append(i)
    print(*u,end=" ")
    print(*k,end=" ")
    print()