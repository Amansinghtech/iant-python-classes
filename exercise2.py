# multiple inheritence

class A:

    def __init__(self) -> None:
        print("class A init is called")

    def feature1(self):
        print("this is feature 1")


class B:
    def __init__(self) -> None:
        print("class B init is called")

    def feature2(self):
        print('this is feature 2')


class C (A, B):
    def __init__(self) -> None:
        super().__init__()
        print("class C init is called")

    def feature3(self):
        print("this is feature 2")


test = C()

test.feature1()
test.feature2()
test.feature3()
