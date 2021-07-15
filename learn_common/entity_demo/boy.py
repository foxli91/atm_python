from learn_common.entity_demo.human import Human


class Boy(Human):

    def __init__(self, package: str, name: str, age: int, address: str, sex: str) -> None:
        super().__init__(name, age, address, sex)
        self.package = package


if __name__ == '__main__':
    b = Boy('迪士尼书包', '张三', 15, '成都市', '男')
    print(b.package)
    print(b.sex)
