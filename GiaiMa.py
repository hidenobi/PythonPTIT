T = int(input())
for i in range(T):
    s = input()
    for j in range(1,len(s),2):
        count = int(s[j])
        while count>0:
            print(s[j-1],end="")
            count-=1
    print()        
