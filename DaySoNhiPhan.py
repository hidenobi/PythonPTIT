N = int(input())
arr = list(int(i) for i in input().split())
count = 0
for  i in range(1, N):
    if (arr[i] != arr[i-1]):
        count = count + 1
print(count)