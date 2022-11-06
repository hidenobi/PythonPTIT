


class SV:
    NUM_SV = 0
    def __init__(self, name, f, s, t):
        SV.NUM_SV += 1
        self.id = "SV" + '{:02d}'.format(SV.NUM_SV)
        self.ave = round((f * 3 + s * 3 + t * 2) / 8 + 0.001, 2)
        self.name = name
    def __str__(self):
        return self.id + ' ' + self.name + " " + '{:.2f}'.format(self.ave)
l = list()
n = int(input())
for i in range(n):
    name = ' '.join(input().strip().title().split())
    f = float(input())
    s = float(input())
    t = float(input())
    l.append(SV(name, f, s, t))
l = sorted(l, key=lambda x: (-x.ave, x.id))
rank = 1
for i in range(n):
    print(l[i], end=' ')
    if i == 0 or l[i].ave == l[i - 1].ave:
        print(rank)
    else:
        print(i + 1)
        rank = i + 1
