from itertools import permutations 
T = int(input())
for t in range(T):
    n = int(input())
    a = []
    for i in range(1,n+1):
        a.append(str(i))
    # a = [1,2]
    p = list(permutations(a))
    print(len(p))
    #slice string
    # hello
    # 01234
    # -5-4-3-2-1
    # p[start:end:step<0]
    # p[-1:-5:-1]=p[::-1]
    for i in p[::-1]:
        # print(type(i))
        x = "".join(i)
        # i = (1,2,3)
        # 1xx2xx3
        print(x,end=' ')
    print()
