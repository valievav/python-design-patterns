class Person:
    def __init__(self):
        # address
        self.street = None
        self.post_code = None
        self.city = None

    def __str__(self):
        return f'Address: {self.post_code}, {self.city}, {self.street}.'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

# different builders for separate attributes


# inherits from PersonBuilder
class PersonAddressCityBuilder(PersonBuilder):
    def in_city(self, city):
        self.person.city = city
        return self


# inherits from previous builder - contains in_city
class PersonAddressPostCodeBuilder(PersonAddressCityBuilder):
    def with_post_code(self, post_code):
        self.person.post_code = post_code
        return self


# inherits from previous builder - contains in_city + with_post_code
class PersonAddressStreetCodeBuilder(PersonAddressPostCodeBuilder):
    def at(self, street):
        self.person.street = street
        return self


# using last builder that contains all methods from prev. chain of builders
# PersonAddressStreetCodeBuilder <- PersonAddressPostCodeBuilder <- PersonAddressCityBuilder <- PersonBuilder

pb = PersonAddressStreetCodeBuilder()
person = pb.in_city('Luxemburg').with_post_code('23-456').at('Serpantine Street 14').build()
print(person)
