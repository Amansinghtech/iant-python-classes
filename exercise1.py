# abstraction
# class variable and instance variable

# class variables are bound to the class itself and instance variable are bound the object.
# changing instance variable doesnot change value of other instances variables or class variables.
# changing values of class variable will show effect on all instances of that particular class.
# value of instance variables can be changed by e.g. self.index
# value of class variable is changed by using class name e.g. Student.index
class Student:

    index = 1  # class variable

    def __init__(self) -> None:
        self.rollno = Student.index  # instance variable
        Student.index = Student.index + 1


s1 = Student()
s2 = Student()
s3 = Student()
print(s1.rollno)
print(s2.rollno)
