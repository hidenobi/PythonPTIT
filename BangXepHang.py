import functools

class Student:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit


def cmp(student1, student2):
    if student1.ac < student2.ac:
        return 1
    elif student1.ac == student2.ac:
        if student1.submit > student2.submit:
            return 1
        elif student1.submit == student2.submit:
            if student1.name > student2.name:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

n = int(input())
arr = []
for i in range(n):
    name = input()
    ac, submit = [int(x) for x in input().split()]
    arr.append(Student(name, ac, submit))
arr = sorted(arr, key=functools.cmp_to_key(cmp))
for i in arr:
    print(i.name, i.ac, i.submit)
