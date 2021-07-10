class Dog:
    name = ''
    age = 1

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'名称：{self.name},年龄：{self.age}'

    def bark(self):
        print(f'我是{self.name},我在狂吠')


print(Dog.__base__)
print(Dog.__bases__)
dog1 = Dog('hll1', 5)
print(isinstance(dog1, Dog))
dog2 = Dog('ob', 2)
dog3 = Dog('cgd', 3)
dog4 = Dog('nds', 2)
dog5 = Dog('liuw', 6)
dog_list = [dog1, dog2, dog3, dog4, dog5]
import print_common

new_list = filter(lambda dg: dg.age >= 3, dog_list)
for d in new_list:
    print(d)
print_common.ps()
mx = max(dog_list, key=lambda dg: dg.age)
print(mx)
print_common.ps()
sk = sorted(dog_list, key=lambda dg: dg.age)
for s in sk:
    print(s)
print_common.ps()
fz = reversed(sk)
for s in fz:
    print(s)
print_common.ps()
names = map(lambda dg: dg.name, dog_list)
for i in names:
    print(i)

# import 'time' # 错误的用法
ts = __import__('time')
print(ts.time())

