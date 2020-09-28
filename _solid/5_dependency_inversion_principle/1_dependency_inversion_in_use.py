from enum import Enum
from abc import ABC, abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name = name


# abstract method for implementation
class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))

    def find_all_children_of(self, parent):  # functional implemented in Relationships instead of Research
        for r in self.relations:
            if r[0].name == parent and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module (uses other class functionality)
    def __init__(self, parent: str, browser: RelationshipBrowser):
        for child in browser.find_all_children_of(parent):
            print(f"{parent} has a child called {child}")

    # not dependent on internal implementation anymore!
    # if type changes (e.g. to dict) this class will not need to be changed (all changes will happen in Relationships)


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

r = Research('John', relationships)
