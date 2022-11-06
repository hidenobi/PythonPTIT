class ThiSinh:
    NUM_TS = 0
    def __init__(self, name, mark, ethnic, region):
        ThiSinh.NUM_TS += 1
        self.id = "TS" + '{:02d}'.format(ThiSinh.NUM_TS)
        self.region = region
        self.ethnic = ethnic
        self.mark = mark
        self.name = name
        if self.ethnic.upper() != 'KINH': self.mark += 1.5
        if self.region == 1: self.mark += 1.5
        if self.region == 2: self.mark += 1
    def __str__(self):
        return self.id + " " + self.name + " " + '{:.1f}'.format(self.mark) + ' ' + ("Do" if self.mark >= 20.5 else "Truot")

l = list()
n = int(input())
for i in range(n):
    name = ' '.join(input().strip().title().split())
    mark = float(input())
    ethnic = input()
    region = int(input())
    l.append(ThiSinh(name, mark, ethnic, region))
l = sorted(l, key=lambda x: (-x.mark, x.id))
for i in l: print(i)
