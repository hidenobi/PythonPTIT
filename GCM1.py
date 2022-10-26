import math


t=int(input())
a=[]
while len(a)<t:
	a.extend(list(map(int,input().split())))
maxx = -10000009
for i in range(len(a)-1):
    maxx = max(maxx,math.gcd(a[i],a[i+1]))
print(maxx)