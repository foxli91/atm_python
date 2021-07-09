from typing import Any


class Student:
    __sex = 'female'

    def __init__(self, name, birth, address, money, courses: []) -> None:
        super().__init__()
        self.name = name
        self.birth = birth
        self.address = address
        self.__money = money
        self.courses = courses

    def __str__(self) -> str:
        cl = '['
        for i in self.courses:
            cl += i.__str__()
        cl += ']'
        return f'学生名称：{self.name},学生生日：{self.birth},学生家庭地址：{self.address},报的课程是{cl}'

    def get_money(self):
        return self.__money

    '''设置金额'''

    def set_money(self, money):
        self.__money = money

    # def __setattr__(self, name: str, value: Any) -> None:
    #     super().__setattr__(name, value)


# Student.__sex = 'aaa'

print(type(Student))
