T = int(input())
for t in range(T):
    N = int(input())
    arr = list(int(i) for i in input().split())
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
        
    for i in dict.items():
        if i[1] % 2:
            print(i[0])
            break