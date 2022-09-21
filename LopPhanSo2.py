import math

a,b,c,d = map(int, input().split())

x = a*d + b*c
y = b*d

print(str(x//math.gcd(x,y)) + '/'+str(y//math.gcd(x,y)))