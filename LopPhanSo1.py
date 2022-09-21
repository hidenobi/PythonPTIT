import math

def rutgon(a, b):
    return (a//math.gcd(a,b), b//math.gcd(a,b))

a, b= map(int, input().split())
res = rutgon(a,b)
print(str(res[0]) + '/' + str(res[1]))