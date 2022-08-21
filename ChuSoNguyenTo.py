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


def isCheck(s):
    if is_prime(len(s)) == False:
        return False
    count = 0
    for i in s:
        if (i == '2' or i == '3' or i == '5' or i == '7'):
            count += 1
    return (2*count > len(s))


T = int(input())
for t in range(T):
    s = input()
    if isCheck(s):
        print("YES")
    else:
        print("NO")
