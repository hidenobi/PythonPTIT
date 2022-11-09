from itertools import permutations
a = list(input().split())
T = int(a[0])
n = int(a[1])
for i in range(T):
    a = list(input().split())
    x = int(a[0])
    y = int(a[1])
    x = str(int(bin(x)[2::]))
    y = str(int(bin(y)[2::]))
    while n > len(y):
        y = "0"+y
    while len(x) < n:
        x = "0"+x
    while n < len(x):
        x = x[1::]
    while n < len(y):
        y = y[1::]
    u = x
    v = y
    x = sorted(list(permutations(x)))
    y = sorted(list(permutations(y)))
    ok = 0
    for k in x:
        tmp = ""
        for h in k:
            tmp+=h
        if tmp == v: 
            ok = 1
            break
    print(ok)
    # chua dung het test
