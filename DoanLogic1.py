t=int(input())
a=[]
while len(a)<t:
	a.extend(list(map(int,input().split())))
for x in a:
	print(2**(x-1)+1)