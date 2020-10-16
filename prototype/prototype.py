import copy


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}.'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


paul = Person('Paul', Address('123 Dune Slide', 'Arrakeen', 'Arrakis'))
print(paul)

alia = copy.deepcopy(paul)  # deepcopy - new obj as prototype
alia.name = 'Alia'
alia.address.street = "1234 Dune Slide"
print("---")
print(paul)
print(alia)
