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
    # python 中没有重载这一说具体原因看笔记
    # def __int__(self):
    #     print('hello')
    #     print(self)


bench = Car()
print(bench)
