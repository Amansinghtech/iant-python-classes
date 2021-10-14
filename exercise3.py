# encapsulation
class A:
    def __init__(self) -> None:
        self.unprotected = "Hi i am unprotected"
        self.__private = "hi i am private"

    def A_method(self):
        print(self.__private)


test = A()

# can be change with the parent class instance or by derived class instance
# test.unprotected = "hi unprotected can be changed"
print(test.unprotected)

# cannot be change with the parent class instance or by derived class instance
# print(test.__private)

test.A_method()
