from multiprocessing import set_forkserver_preload


class GV:
    score = 0
    status = ""
    monHoc = ""
    def __init__(self, id,name,maXetTuyen,diemTin,diemChuyenMon) :
        self.id = id
        self.name = name
        self.maXetTuyen = maXetTuyen
        self.diemTin = diemTin
        self.diemChuyenMon = diemChuyenMon
        if self.maXetTuyen[1]=='1': self.score = self.diemTin*2+self.diemChuyenMon+2
        elif self.maXetTuyen[1]=='2': self.score = self.diemTin*2+self.diemChuyenMon+1.5
        elif self.maXetTuyen[1]=='3': self.score = self.diemTin*2+self.diemChuyenMon+1
        else: self.score = self.diemTin*2+self.diemChuyenMon
        if self.maXetTuyen[0]=='A': self.monHoc = 'TOAN'
        elif self.maXetTuyen[0]=='B': self.monHoc = 'LY'
        else: self.monHoc = 'HOA'
        if self.score >= 18: self.status = 'TRUNG TUYEN'
        else: self.status = "LOAI"
    def __str__(self) -> str:
        return self.id + " "+self.name+" "+self.monHoc+" "+str(self.score)+" "+self.status
n = int(input())
a = []
for i in range(n):
    id = "GV"
    if i+1<10: id+="0"+str(i+1)
    else: id+=str(i+1)
    name = input()
    maXetTuyen = input()
    diemTin = float(input())
    diemChuyenMon = float(input())
    a.append(GV(id,name,maXetTuyen,diemTin,diemChuyenMon))
a=sorted(a,key=lambda x: -x.score)
for i in a:
    print(i)
