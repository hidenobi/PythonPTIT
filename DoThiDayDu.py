def subtracList(a, b, i):
    return list(filter(lambda x: x not in a and x != i, b))


n = int(input())
m = int(input())
a = []
b = []
for i in range(n+1):
    a.append([])
    if i != 0:
        b.append(i)
for i in range(m):
    u, v = [int(x) for x in input().split()]
    a[u].append(v)
    a[v].append(u)
isCheck = 1
print(a)
for i in range(1, n+1):
    # a[i] = subtracList(a[i], b, i)
    a[i] = b
    for j in range(1,n+1):
        if j !=i :
            try:
                a[j].remove(i)
            except:
                pass
    if (len(a[i]) != n-1):
        print("NO")
        isCheck = 0
        break
if isCheck == 1:
    print("YES")
print(a)
