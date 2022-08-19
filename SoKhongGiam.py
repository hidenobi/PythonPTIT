def isNotDecreaseNumber(number):
    for i in range(len(number)-1):
        if(number[i]>number[i+1]): return False
    return True
T = int(input())
for i in range(T):
    str = input()
    if(isNotDecreaseNumber(str)): print("YES")
    else: print("NO")
