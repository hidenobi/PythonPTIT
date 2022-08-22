T = int(input())
for t in range(T):
    s = input()
    ans = 1
    for i in s:
        if(i!='0'):
            ans*=int(i)
    print(ans)