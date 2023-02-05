from abc import ABC, abstractmethod


class Super(ABC):
    Value1 = False
    Value2 = False

    def test_method(self):
        print("Super Class")


class Sub(Super):
    Value2 = True

    def __init__(self):
        if self.Value1:
            print("Yes")
            print(self.Value1)
            print(self.Value2)
        else:
            print("No")
            print(self.Value1)
            print(self.Value2)

    def test_method(self):
        print("Sub Class")


s = Sub()
s.test_method()
