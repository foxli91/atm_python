from typing import Any

from Dog import Dog

class Car:
    color = ''
    price = 0.0
    car_type = ''
    brand = ''
    owner = 'Jimmy'

    def __init__(self, color, price, car_type, brand, dog: Dog):
        self.color = color
        self.price = price
        self.car_type = car_type
        self.brand = brand
        self.pet = dog

    def say_hello(self):
        print('say hello 啊')
        print(f'self-owner {self.owner}')

    def set_dog(self, dog: Dog):
        self.pet = dog
        self.pet.bark()

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __str__(self) -> str:
        return super().__str__() + '' + f'color={self.color},price={self.price},car_type={self.car_type},brand={self.brand}'

    # python 中没有重载这一说具体原因看笔记
    # def __int__(self):
    #     print('hello')
    #     print(self)
    # def to_string(self):
    #     return f'color={self.color},price={self.price},car_type={self.car_type},brand={self.brand}'


dog = Dog('就是', 1)
bench = Car('黑色', 78904.6, 'SUV', '奔驰', dog)
#
# bench.set_dog(dog)
print(bench)
print(bench.__str__())
# bench.age = 15
# print(bench.age)
# print(bench.ages)
bmw = Car('红色', 18904.6, '轿车', '宝马', dog)
audio = Car('白色', 36784.6, '轿车', '奥迪', dog)

# print(id(Car.say_hello))
print(bench.say_hello)
print(bench)
print(audio.say_hello)
print(bmw.say_hello)
print('-----------------------owner------------')
print(Car.owner)
print(bench.owner)
print(audio.owner)
print(bmw.owner)
bench.owner = 'Lishuai'
print('-----------------------修改某个owner------------')
print(Car.owner)
print(bench.owner)
print(audio.owner)
print(bmw.owner)
# print(id(Car.owner))
# print(id(bench.owner))
# print(id(audio.owner))
# print(id(bmw.owner))
