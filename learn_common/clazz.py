from student import Student


class Clazz:
    def __init__(self, name, address) -> None:
        super().__init__()
        self.name = name
        self.address = address
        self.student_list = []

    def add_student(self, student: Student):
        self.student_list.append(student)

    def __str__(self) -> str:
        st_list = '['
        for i in self.student_list:
            st_list += i.__str__() + '\n'
        st_list += ']'
        return f'班级名称:{self.name},\n班级学生列表:{st_list}'
