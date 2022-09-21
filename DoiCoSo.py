xchange = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def change(x, k):
    res = ''
    while (x > 0):
        r = x % k
        res = xchange[r] + res
        x = int(x/k)
    return res
T = int(input())
for t in range(T):
    x, k = map(int,input().split())
    print(change(x, k))