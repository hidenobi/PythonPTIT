def check(s1, s2):
    for i in range(1, len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            return 'NO'
    return 'YES'

T = int(input())
for t in range(T):
    s = input()
    print(check(s, s[::-1]))