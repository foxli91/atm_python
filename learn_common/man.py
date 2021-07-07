class Man:
    def __init__(self, name, height, sex, weight) -> None:
        super().__init__()
        self.name = name
        self.height = height
        self.sex = sex
        self.weight = weight

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


import print_common

m = Man('张三', 1.75, '男', 75)
print(m.bmi)
