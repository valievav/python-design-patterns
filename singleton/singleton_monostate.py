# NOTE: this solution is just FYI, better to use decorator or metaclass


# 1st way - have attr values in class var
class CEO:
    __shared_state = {  # all data in static variable
        'name': 'Leon',
        'age': 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state  # copy of the reference to the common dict

    def __str__(self):
        return f"{self.name}, {self.age}"


# 2nd way - base class with shared_state
class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}."


if __name__ == "__main__":
    # 1st way with class attr
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77  # value in shared var is updated
    print(ceo1)
    print(ceo2)

    # 2nd way with base class
    cfo1 = CFO()
    cfo1.name = "Sharyl"
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Lana"  # attr value udated to all classes that inherit base class
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep='\n')  # both are Lana

    # conclusion - monostate has its drawbacks, better to use decorator or metaclass
