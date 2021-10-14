# abstraction
# handle complexity by hiding unnecessary details from the user.User is familiar with that "what function does" but they don't know "how it does."

# A class consists of one or more abstract method is called the abstract class.
# Abstract method do not contain their implementation.
# Abstract classes are meant to be blueprint of the other class.
# we cannot create instance of abstract method

from abc import ABC, abstractmethod


class parent(ABC):

    @abstractmethod
    def execute(self):
        pass


class child(parent):

    def execute(self):
        print("executing...")


test = child()
test.execute()
