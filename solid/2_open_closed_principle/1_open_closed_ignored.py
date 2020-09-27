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


class ProductFilter:
    def filter_by_color(self, products, color):
        return [product.name for product in products if product.color == color]

    def filter_by_size(self, products, size):
        return [product.name for product in products if product.size == size]

    def filter_by_color_and_size(self, products, color, size):
        return [product.name for product in products if product.color == color and product.size == size]

    # each time new filter is added we'll need to modify ProductFilter
    # possible any combination (and, or, none, either, with new parameter etc.) and each will require new method


if __name__ == "__main__":
    book = Product('book', Color.BLUE, Size.MEDIUM)
    journal = Product('journal', Color.GREEN, Size.MEDIUM)
    sketchbook = Product('sketchbook', Color.GREEN, Size.LARGE)
    products = [book, journal, sketchbook]

    f = ProductFilter()
    print(f"Filter by color GREEN: {f.filter_by_color(products, Color.GREEN)}")
    print(f"Filter by size MEDIUM: {f.filter_by_size(products, Size.MEDIUM)}")
    print(f"Filter by color GREEN and size LARGE: {f.filter_by_color_and_size(products, Color.GREEN, Size.LARGE)}")

    assert f.filter_by_color(products, Color.GREEN) == ['journal', 'sketchbook']
    assert f.filter_by_size(products, Size.MEDIUM) == ['book', 'journal']
    assert f.filter_by_color_and_size(products, Color.GREEN, Size.LARGE) == ['sketchbook']
