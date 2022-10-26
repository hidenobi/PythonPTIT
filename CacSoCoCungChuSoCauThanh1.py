from itertools import permutations


T = int(input())
for t in range(T):
    a, b = input().split()
    x = sorted(list(permutations(a)))
    y = sorted(list(permutations(b)))
    if a[0] == '0' or b[0] == '0':
        print("False")
    elif x == y:
        print("True")
    else:
        print("False")

