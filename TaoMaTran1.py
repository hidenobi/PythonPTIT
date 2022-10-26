n = int(input())
a = []
for i in range(n//2):
    b = []
    for j in range(n//2):
        b.append(j+1)
    for j in range(n//2, n):
        b.append(0)
    a.append(b)
for i in range(n//2, n):
    b = []
    for j in range(n//2):
        b.append(0)
    for j in range(n//2, n):
        b.append(n-j)
    a.append(b)
for i in a:
    for j in i:
        print(j, end=" ")
    print()
