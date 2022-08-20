T = int(input())
for t in range(T):
    s = input()
    x = s[-1:-3:-1]
    y = x[::-1]
    if(y=='86'): print("YES")
    else: print("NO")