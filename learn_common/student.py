class Student:
    name = '张安琪'

    def get_name_str(self):
        return self.name

    def spe(self):
        print('-------哈哈哈')


st = Student()
print(st.name)
st.spe()
