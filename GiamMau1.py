a = list(input().split())
M = int(a[0])
N = int(a[1])
c = int(a[2])
b = int(a[3])
a = []
for i in range(M):
    d = [int(x) for x in input().split()]
    a.append(d)
for i in range(0,M,c):
    for j in range(0,N,b):
        print(a[i][j],end=" ")
    print()


