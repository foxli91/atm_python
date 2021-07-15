class Human:
    def __init__(self, name: str, age: int, address: str, sex: str) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.sex = sex

    def __str__(self) -> str:
        return super().__str__()


if __name__ == '__main__':
    h = Human('张三', 15, '北京市朝阳区', '男')
    print(h.name, h.address, h.age, h.sex)
