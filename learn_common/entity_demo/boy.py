from learn_common.entity_demo.human import Human


class Boy(Human):

    #
    # def __init__(self, package: str) -> None:
    #     self.package = package

    def __init__(self, package: str, name: str, age: int, address: str, sex: str) -> None:
        '''
         这里第一行必须遵循规范调用父类的构造方法
        '''
        super().__init__(name, age, address, sex)
        self.package = package


if __name__ == '__main__':
    # b = Boy('迪士尼书包', '张三', 15, '成都市', '男')
    b = Boy('迪士尼书包')
    print(b.package)
    print('sex=', b.sex)
