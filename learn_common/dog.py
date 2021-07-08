class Dog:
    name = ''
    age = 1

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def bark(self):
        print(f'我是{self.name},我在狂吠')


print(Dog.__base__)
print(Dog.__bases__)
