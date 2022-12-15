def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True
n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if is_prime(i):
        b.append(i)
b.sort()
j = 0
for i in a:
    if i in b:
        print(b[j],end=" ")
        j+=1
    else:
        print(i,end=" ")
