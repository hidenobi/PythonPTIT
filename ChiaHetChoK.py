[a,K,N]=map(int,input().split())
mod = a % K
mod = K - mod
x = 0
if a+x*K+mod > N :
    print(-1)
while a+x*K+mod <= N:
    print(x*K+mod,end=" ")
    x+=1