T = int(input())
for t in range(T):
    n = int(input())
    arr1 = list(int(i) for i in input().split())
    arr2 = list(int(i) for i in input().split())
    arr1.sort()
    arr2.sort()
    check = 'YES'
    for i in range(0, n):
        if arr1[i] > arr2[i]:
            check = 'NO'
            break
    print(check)