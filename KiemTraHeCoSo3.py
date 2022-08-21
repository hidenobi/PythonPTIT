def isTenaryNumber(s):
    for i in s:
        if i != '0' and i != '2' and i != '1':
            return False
    return True


T = int(input())
for t in range(T):
    s = input()
    if isTenaryNumber(s):
        print("YES")
    else:
        print("NO")
