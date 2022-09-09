from datetime import date
import math
from msilib.schema import Binary
import re
def BMI():
    w = int(input())
    h = float(input())
    print(w/(h*h))
def Age():
    year = int(input())
    print(date.today().year-year)
def GPA():
    score = float(input())
    num = int(input())
    print(score/num)
s= "^[Bb]{1}\\d{2}[A-Za-z]{4}\\d{3}$"
x = 'B20DCCN622'
print(re.search(s,x))

