from typing import Any

import print_common


class Parent1:
    x = 111
    __y = 222

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def got_y(self):
        return self.__y


class Parent2:
    def __hello(self):
        print('say--Hello')

    def to_say(self):
        self.__hello()


class Sub1(Parent1):
    pass


class Sub2(Parent1, Parent2):
    # pass
    def prf(self):
        print()
        print(self.x)


s1 = Sub1()
print(s1)
print(Sub2.mro())
s1.__setattr__('x', 123232)
print(s1.x)
print(s1.got_y())
# print(Sub1.__bases__)
# print(Sub2.__bases__)
# print(Parent1.__bases__)
p2 = Parent2()
p2.to_say()
