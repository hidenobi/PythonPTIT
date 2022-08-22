from operator import le


T = int(input())
for t in range(T):
    s = input()
    totalDigitNumber = 0
    for i in s:
        totalDigitNumber += int(i)
    totalDigitNumber = str(totalDigitNumber)
    tmp = totalDigitNumber[::-1]
    if (totalDigitNumber == tmp and len(tmp)>1):
        print("YES")
    else:
        print("NO")
