from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


#### USED SPECIFICATION PATTERN

# 1 - Prepare base classes (to be able to add different kind of Specification and Filter later on)
class Specification:
    """
    Base specification. Defines whether item satisfies particular criteria.
    """
    def is_satisfied(self, item):
        pass


class Filter:
    """
    Base class for filter.
    """
    def filter(self, items, spec):
        pass


# 2 - Prepare spec and filter classes
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    """
    Combinator AND.
    """
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return all([spec for spec in self.specs if spec.is_satisfied(item)])


class ProductFilter(Filter):
    def filter(self, items, spec):
        return [item.name for item in items if spec.is_satisfied(item)]


# when need to add new parameter to filter (e.g. by weight), no changes to the existing classes required,
# only create WeightSpecification and pass it to the filter
# when need to add new filter (e.g. color or size), no changes to the existing classes required,
# only create separate OrSpecification


if __name__ == "__main__":
    book = Product('book', Color.BLUE, Size.MEDIUM)
    journal = Product('journal', Color.GREEN, Size.MEDIUM)
    sketchbook = Product('sketchbook', Color.GREEN, Size.LARGE)
    products = [book, journal, sketchbook]

    spec_green = ColorSpecification(Color.GREEN)
    spec_medium = SizeSpecification(Size.MEDIUM)
    spec_large = SizeSpecification(Size.LARGE)
    spec_green_and_large = AndSpecification(spec_green, spec_large)

    f = ProductFilter()
    print(f"Filter by color GREEN: {f.filter(products, spec_green)}")
    print(f"Filter by size MEDIUM: {f.filter(products, spec_medium)}")
    print(f"Filter by color GREEN and size LARGE: {f.filter(products, spec_green_and_large)}")

    assert f.filter(products, spec_green) == ['journal', 'sketchbook']
    assert f.filter(products, spec_medium) == ['book', 'journal']
    assert f.filter(products, spec_green_and_large) == ['sketchbook']
