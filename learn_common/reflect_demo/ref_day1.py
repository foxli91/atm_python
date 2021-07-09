from learn_common.student import Student
from learn_common.print_common import ps

st1 = Student('张世坤', '1992-08-18', '武汉市', 1500, [])
ps()
# print(st1)
# print(dir(st1))
# print(dir(Student))

# hasattr(对象, '字符串属性名')
# setattr(对象, '字符串属性名', '数值')
# getattr(对象, '字符串属性名','如果没有返回默认值')
# delattr(对象,'字符串属性名')

print(hasattr(st1, 'name'))
setattr(st1, 'name', '李海生')
print(getattr(st1, 'name'))
print(delattr(st1, 'name'))
print(hasattr(st1, 'name'))
ps()
print(getattr(st1, 'get_money'))
print(getattr(Student, 'get_money'))

print(getattr(st1, 'get_money')())

st1.__setattr__('money', 600000)
print(st1.get_money())

st1.__setattr__('name', 600000)
print(st1.name)
