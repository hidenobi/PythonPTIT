def isPretty(a):
    for i in range(2, len(a), 2):
        if (a[i] != a[0]): return False
    for i in range(3, len(a), 2):
        if (a[i] != a[1]): return False
    return True
T = int(input())
for t in range(T):
    if isPretty(input()): print('YES')
    else: print('NO') 