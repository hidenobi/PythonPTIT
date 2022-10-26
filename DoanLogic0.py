t=int(input())
a=[]
while len(a)<t:
	a.extend(list(map(int,input().split())))
for x in a:
	print(x*(x+1))