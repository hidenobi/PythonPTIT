from datetime import datetime
date_format = "%d/%m/%Y"

class KhachSan:
    tongtien = 0
    soNgay = 0

    def __init__(self, ma, ten, soPhong, ngayNhan, ngayTra, phiDichVu):
        self.ma = ma
        self.ten = ten
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.phiDichVu = phiDichVu
        a = datetime.strptime(self.ngayTra, date_format)
        b = datetime.strptime(self.ngayNhan, date_format)
        d = a - b
        self.soNgay = d.days+1
        if (self.soPhong[0] == '1'):
            self.tongtien = 25*self.soNgay+self.phiDichVu
        elif self.soPhong[0] == '2':
            self.tongtien = 34*self.soNgay+self.phiDichVu
        elif self.soPhong[0] == '3':
            self.tongtien = 50*self.soNgay+self.phiDichVu
        else:
            self.tongtien = 80*self.soNgay+self.phiDichVu

    def __str__(self):
        return self.ma + " " + self.ten + " " + self.soPhong + " " + str(self.soNgay) + " " + str(self.tongtien)


n = int(input())
a = []
for i in range(n):
    ma = "KH"
    if i+1 < 10:
        ma += "0"+str(i+1)
    else:
        ma += str(i+1)
    ten = input().strip()
    soPhong = input().strip()
    ngayNhan = input().strip()
    ngayTra = input().strip()
    phiDichVu = int(input())
    a.append(KhachSan(ma, ten, soPhong, ngayNhan, ngayTra, phiDichVu))
a = sorted(a, key=lambda x: -x.tongtien)
for i in a:
    print(i)
