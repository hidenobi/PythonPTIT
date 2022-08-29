from itertools import permutations
s = input()
res = permutations(s)
for i in res:
    print(*i, sep ='')