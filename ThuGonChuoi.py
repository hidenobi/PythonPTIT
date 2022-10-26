n = int(input())
while n:
    n -= 1
    s = input().split("\\")
    print(s[0] + "\\..\\" + s[-1])
