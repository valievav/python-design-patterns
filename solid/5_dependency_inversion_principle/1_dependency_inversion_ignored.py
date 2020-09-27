from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name = name


class Relationships:  # low-level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))


class Research:  # high-level module (uses other class functionality)
    def __init__(self, parent: str, relationships: Relationships):
        relations = relationships.relations

        for r in relations:
            if r[0].name == parent and r[1] == Relationship.PARENT:
                print(f"{parent} has a child called {r[2].name}")

    # relations is a dependency from Relationships low-level module
    # if it changes (e.g. to dict) it will cause this class changes


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

r = Research('John', relationships)
