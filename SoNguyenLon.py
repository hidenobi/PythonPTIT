t = int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    print(b)