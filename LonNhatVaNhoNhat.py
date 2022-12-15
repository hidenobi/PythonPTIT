while True:
    n = int(input())
    if( n==0):
        break
    a = []
    for i in range(n):
        x = input()
        while(x[0]=='0') and x!='0':
            x = x[1::]
        a.append(x)
    a.sort(key=lambda x: (len(x),x))
    if a[0] == a[len(a)-1]:
        print("BANG NHAU")
    else:
        print(a[0]+" "+a[len(a)-1])