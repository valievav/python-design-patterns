# Write a function called is_singleton() that takes factory method
# and returns True/False depending on whether the object is a singleton or not.


class Singleton(type):  # metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FactorySingleton(metaclass=Singleton):
    def __init__(self):
        pass


class Factory:
    def __init__(self):
        pass


def is_singleton(factory):
    f1 = factory()
    f2 = factory()
    return f1.__hash__() == f2.__hash__()


print(is_singleton(FactorySingleton))
print(is_singleton(Factory))
