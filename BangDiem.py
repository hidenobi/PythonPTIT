from decimal import ROUND_HALF_UP, Decimal

id = 1
class HocSinh :
    maHS = 'HS'
    GPA = 0
    rating = ''
    def __init__(self, name, score) :
        global id
        self.maHS += '{:02d}'.format(id)
        id += 1
        self.name = name
        x = 2 * score[0] + 2 * score[1]
        for i in range(2, 10) :
            x += score[i]
        x /= 12
        if x < 5 : self.rating = 'YEU'
        elif x < 7 : self.rating = 'TB'
        elif x < 8 : self.rating = 'KHA'
        elif x < 9 : self.rating = 'GIOI'
        else : self.rating = 'XUAT SAC'
        self.GPA = x.quantize(Decimal('0.1'), ROUND_HALF_UP)

    def toString(self) :
        print(self.maHS, self.name, self.GPA, self.rating)

n = int(input())
a = []
for i in range(n) :
    b = input()
    c = [Decimal(x) for x in input().split()]
    a.append(HocSinh(b, c))

a = sorted(a, key= lambda x : (- x.GPA, x.maHS))
for i in a :
    i.toString()