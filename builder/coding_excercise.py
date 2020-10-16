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


class CodeBuilder:
    indent = ' '

    def __init__(self, root_name):
        self.obj = eval(root_name)()  # instantiate class

    def get_obj_attrs(self):
        obj_attrs = {k: v for k, v in self.obj.__dict__.items() if not k.startswith('__')}
        return obj_attrs

    def add_field(self, field, value):
        if field in self.get_obj_attrs().keys():
            try:
                setattr(self.obj, field, value)  # set attr
            except AttributeError:
                print('No such attribute.')
            return self

    def __str__(self):
        lines = []
        lines.append(f"class {self.obj.__class__.__name__}:")
        lines.append(f"{self.indent * 2} def __init__(self):")
        for field, value in self.get_obj_attrs().items():
            lines.append(f'{self.indent * 4}{field} = {value}')

        return str('\n'.join(lines))


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
