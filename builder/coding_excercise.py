# You are asked to implement the Builder design pattern for rendering simple chunks of code.
# Sample use of the builder you are asked to create:
# cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
# print(cb)
#
# The expected output:
# class Person:
# def __init__(self):
# self.name = ""
# self.age = 0
import inspect


class CodeBuilder:
    def __init__(self, root_name):
        self.obj = eval(root_name)()  # instantiate class

    def add_field(self, field, value):
        try:
            setattr(self.obj, field, value)  # set attr
        except AttributeError:
            print('No such attribute.')
        return self

    def __str__(self):
        return str(self.obj)


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
# TODO -print code
