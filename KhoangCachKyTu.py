import math


def isCheck(s,x):
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(x[i])-ord(x[i-1])): return False
    return True
T = int(input())
for t in range(T):
    s = input()
    # đảo xâu
    x = s[::-1] 
    if(isCheck(s,x)): print("YES")
    else: print("NO")