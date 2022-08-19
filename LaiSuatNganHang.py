T = int(input())
for i in range(T):
    [N,X,M] = map(float,input().split())
    ans = 0;
    while N < M:
        N = N*(1+X/100)
        ans+=1
    print(ans) 
    

