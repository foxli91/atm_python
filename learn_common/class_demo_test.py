from clazz import Clazz
from student import Student
from course import Course

if __name__ == '__main__':
    print('我是自己运行的')

else:
    print('我是模块运行的')

cl1 = Clazz('2011级5班', '成都市')
cou1 = Course('linux运维', 14000, '10')
cou2 = Course('python', 25000, '14')
cou3 = Course('Java', 28000, '15')
cou4 = Course('前端', 24000, '12')
cou5 = Course('C++', 32000, '24')
st1 = Student('张兵', '1995-07-01', '成都市金牛区', 7500, [cou1, cou4])
st2 = Student('刘长久', '1992-12-11', '成都市金牛区', 17500, [cou3, cou2])
st3 = Student('鄢俊', '1994-09-16', '成都市金牛区', 3500, [cou2, cou5])
cl1.add_student(st1)
cl1.add_student(st2)
cl1.add_student(st3)
print(cl1)
