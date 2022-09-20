s1 = input()
s2 = input()
vt = int(input()) - 1
check = True
for i in range(0, len(s1)):
    if (i == vt):
        print(s2, end = '')
        check = False
    print(s1[i], end = '')
if check: print(s2)