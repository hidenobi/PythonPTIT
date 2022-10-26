T = int(input())
for t in range(T):
    a, b = input().split()
    a = a.lower()
    b = b.lower()
    x = 0
    y = 0
    for i in a:
        tmp = ord(i)-97
        x = x*26+tmp
    for i in b:
        tmp = ord(i)-97
        y = y*26+tmp
    z = x+y
    ans=""
    while z!=0:
        r = z%26
        z//=26
        ans+=chr(r+97)
    print(ans[::-1])
    
