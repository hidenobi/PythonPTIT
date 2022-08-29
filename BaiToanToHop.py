from itertools import combinations

n,k = map(int, input().split())
l = list(set(int(x) for x in input().split()))
l.sort()
res = combinations(l,k)
for i in res:
    print(*i)