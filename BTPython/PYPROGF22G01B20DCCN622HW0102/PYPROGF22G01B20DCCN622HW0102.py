"""
Họ tên: Vo Huu Tuan
Mã Sinh Viên: B20DCCN622
Mã nhóm: G01
"""

from collections import Counter
# do không máy em không rút gọn đường dẫn mà thêm phần phía trước nên em không thêm ./PYPROGF22G01B20DCCN622HW0102 được ạ
with open('G18LogAllDownload202210142034ForProcess.txt', 'r') as rfile, open('result.txt', 'w', encoding='utf-8') as wfile:
    listSV = []
    listTerms = []
    lines = rfile.readlines()
    for line in lines:
        if "B18DCDT" in line:
            list_word = line.split("B18DCDT")
            terms = "B18DCDT" + list_word[1][0:3]
            if "txt" in list_word[1] or "wav" in list_word[1]:
                exten_word = list_word[1].split(".")
                listTerms.append(terms+exten_word[1][0:3])
            if terms not in listSV:
                listSV.append(terms)
    cnt_sv_file = dict(Counter(listTerms))
    listStudents = {}
    for sv in listSV:
        if cnt_sv_file.get(sv+'wav') and cnt_sv_file.get(sv+'txt'):
            listStudents[sv] = [
                {'nWavFile': cnt_sv_file[sv+'wav']}, {'nTxtFile': cnt_sv_file[sv+'txt']}]
        elif cnt_sv_file.get(sv+'wav'):
            listStudents[sv] = [
                {'nWavFile': cnt_sv_file[sv+'wav']}, {'nTxtFile': 0}]
        elif cnt_sv_file.get(sv+'txt'):
            listStudents[sv] = [{'nWavFile': 0}, {
                'nTxtFile': cnt_sv_file[sv+'txt']}]
        else:
            listStudents[sv] = [{'nWavFile': 0}, {'nTxtFile': 0}]
    for student in listStudents.keys():
        wfile.writelines('===============================\n')
        wfile.writelines(f'{student}\n')
        tmp = listStudents[student][0]['nWavFile']
        wfile.writelines(f'---> {tmp} wav file(s)\n')
        tmp = listStudents[student][1]['nTxtFile']
        wfile.writelines(f'---> {tmp} text file(s)\n')
