N = int(input())
dem = 0

while dem < N:
    topic = input()
    res = 0
    dem += 1
    s = '#'
    while len(s) > 0 and dem < N:
        s = input()
        if len(s)>0: 
            res += 1
        dem += 1
    print(topic+': '+str(res))