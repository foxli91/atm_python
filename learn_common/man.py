from learn_common.print_common import ps


class Man:
    def __init__(self, name, height, sex, weight) -> None:
        # super().__init__()
        self.name = name
        self.height = height
        self.sex = sex
        self.weight = weight
        self.__wife = ''

    def fuxk(self):
        print('fuck you asshole')

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

    @property
    def wife(self):
        return self.__wife

    @wife.setter
    def wife(self, value):
        self.__wife = value

    @wife.deleter
    def wife(self):
        del self.__wife


class Boy(Man):

    def __init__(self, name, height, sex, weight, speak, father) -> None:
        super().__init__(name, height, sex, weight)
        self.speak = speak
        self.father = father

    def get_info(self):
        print(self.name)
        print(self.sex)
        print('父类的呢')
        print(super().name)
        print(super().bmi)
        super().fuxk()


ps()
m = Man('张三', 1.75, '男', 75)
print(m.bmi)
m.wife = '刘美琪'
print(m.wife)
bo = Boy('张冰s', 1.72, '男', 75, '普通话', '张谦')
print(bo.name)
bo.get_info()
