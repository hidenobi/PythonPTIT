n = int(input())
a = [int(x) for x in input().split()]
i = 0
l = len(a)
while i<l-1:
    if (a[i]+a[i+1])%2==0 :
        # print(str(a[i])+" "+str(a[i+1]))
        a.pop(i)
        a.pop(i)
        l = len(a)
        if i > 0:
            i-=1
    else:
        i+=1
print(len(a))
