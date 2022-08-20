from cgi import print_arguments
import math


T = int(input())
for t in range(T):
    a = input()
    x = a[::-1]
    a = int(a)
    x = int(x)
    if (math.gcd(a, x) == 1):
        print("YES")
    else:
        print("NO")
