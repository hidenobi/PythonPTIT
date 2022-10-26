m,n,t=[int(i) for i in input().split()]
a=[]
for i in range(m):
    a.append([])
    b = [int(x) for x in input().split()]
    for x in b:
        a[i].append(x)
        
for i in range(m):
    for j in range(n):
        if a[i][j] > t:
            print(255,end=" ")
        else:
            print(0,end=" ")
    print(end='\n')