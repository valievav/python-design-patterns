# You are given a class Person. The Person has 2 attributes: id and name.
# Implement a PersonFactory that has a non-static create_person() method that takes a person's name
# and return person initialized with this name and an id.
# The id of the person should be set as a 0-based index of the object created.
# So, the first person the factory makes should have id=0, second id=1 and so on.


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print(f"{id}, {name}")


class PersonFactory:
    index = 0

    def create_person(self, name):
        instance = Person(self.index, name)
        self.index += 1
        return instance


f = PersonFactory()
f.create_person('Paul')
f.create_person('Chani')
f.create_person('Jessica')
f.create_person('Danika')
