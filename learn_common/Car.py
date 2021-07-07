from typing import Any


class Car:
    color = ''
    price = 0.0
    car_type = ''
    brand = ''

    def __init__(self, color, price, car_type, brand):
        self.color = color
        self.price = price
        self.car_type = car_type
        self.brand = brand

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


bench = Car('黑色', 78904.6, 'SUV', '奔驰')
print(bench)
print(bench.__str__())
bench.age = 15
print(bench.age)
print(bench.ages)
