n = input()
l = len(n)
while l>1:
    a = int(n[:l//2:])
    b= int(n[l//2::])
    n = a+b
    n = str(n)
    print(n)
    l = len(n)
