class Student:

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
