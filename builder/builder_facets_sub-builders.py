# using sub-builders (drawback: violates Open-Closed principle)


class Person:
    def __init__(self):
        # address
        self.street = None
        self.post_code = None
        self.city = None
        # employment
        self.company = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.post_code}, {self.city}, {self.street}. ' \
               f'Employment info: {self.company}, {self.position}, {self.annual_income}.'


class PersonBuilder:
    def __init__(self, person=Person()):  # reusing the same person
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)  # calls 1st sub-builder

    @property
    def works(self):
        return PersonJobBuilder(self.person)  # calls 2nd sub-builder

    def build(self):
        return self.person


# 1st sub-builder
class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def in_city(self, city):
        self.person.city = city
        return self

    def with_post_code(self, post_code):
        self.person.post_code = post_code
        return self

    def at(self, street):
        self.person.street = street
        return self


# 2nd sub-builder
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company = company
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def with_annual_income(self, annual_income):
        self.person.annual_income = annual_income
        return self

# Flow:
# Person Builder -> lives -> PersonAddressBuilder -> fill in certain attributes of a Person class
#                -> works -> PersonJobBuilder -> fill in certain attributes of a Person class


pb = PersonBuilder()
person = pb.lives.\
    at('Serpantine Street 14').in_city('Luxemburg').with_post_code('23-456').\
    works.at('Company Innovations').as_a('Engineer').with_annual_income(150000).\
    build()

print(person)
# Address: 23-456, Luxemburg, Serpantine Street 14. Employment info: Company Innovations, Engineer, 150000.
