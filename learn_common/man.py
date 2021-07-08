class Man:
    def __init__(self, name, height, sex, weight) -> None:
        super().__init__()
        self.name = name
        self.height = height
        self.sex = sex
        self.weight = weight
        self.__wife = ''

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


import print_common

m = Man('张三', 1.75, '男', 75)
print(m.bmi)
m.wife = '刘美琪'
print(m.wife)
