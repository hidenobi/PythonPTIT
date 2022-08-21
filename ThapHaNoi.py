def HaNoiTower(n,a,b,c):
    if(n==1):
        print(a+" -> "+c)
        return
    HaNoiTower(n-1,a,c,b)
    HaNoiTower(1,a,b,c)
    HaNoiTower(n-1,b,a,c)
n = int(input())
a = 'A'
b = 'B'
c = 'C'
HaNoiTower(n,a,b,c)