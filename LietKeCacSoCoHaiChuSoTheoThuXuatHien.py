s = input()
a = {}
for i in range(1, len(s), 2):
    a[int(s[i-1])*10+int(s[i])] = 1
for i in a.keys():
    print(i, end = ' ')