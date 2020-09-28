class Printer:
    def print(self, document):
        print(f"{self.__class__.__name__}: I am printing")


class Fax:
    def fax(self, document):
        print(f"{self.__class__.__name__}: I am sending/receiving fax.")


class Scanner:
    def scan(self, document):
        print(f"{self.__class__.__name__}: I am scanning.")


class MultiFunctionPrinter(Printer, Fax, Scanner):
    pass


class OldFashionedPrinter(Printer):
    pass


# by breaking Machine onto separate classes and inheriting from them
# we can include only methods that are in use for the object

doc = "Doc"

multi_printer = MultiFunctionPrinter()
multi_printer.print(doc)
multi_printer.fax(doc)
multi_printer.scan(doc)

old_printer = OldFashionedPrinter()
old_printer.print(doc)
