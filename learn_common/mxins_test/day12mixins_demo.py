class Vehicle:  # 交通工具
    pass


class FlyableMixin:
    def fly(self) -> None:
        '''
        飞行功能相应的代码
        '''
        print("I am flying")


class CivilAircraft(FlyableMixin, Vehicle):  # 民航飞机
    pass


class Helicopter(FlyableMixin, Vehicle):  # 直升飞机

    def fly(self) -> None:
        super().fly()
        print('我特么还可以随意飞')


class Car(Vehicle):  # 汽车
    pass


fly = CivilAircraft()
fly.fly()
he = Helicopter()
he.fly()


class People:
    school = '清华大学'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Teacher(People):
    def __init__(self, name, sex, age, title):
        super().__init__(name, age, sex)  # 调用的是绑定方法，自动传入self
        print(super().name)
        # 在Python2中super的使用需要完整地写成super(自己的类名,self) ,而在python3中可以简写为super()。
        self.title = title

    def teach(self):
        print('%s is teaching' % self.name)


class Cpu:
    def read(self):
        pass

    def write(self):
        pass
