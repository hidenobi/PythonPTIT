import re
str = ''
while True:
    try:
        str += input()
    except EOFError:
        break
str = re.split('[.?!]', str)
for i in str:
    if len(i) > 0:
        x = re.sub('\s+',' ',i.strip())
        print(x[0].upper()+x[1:].lower())