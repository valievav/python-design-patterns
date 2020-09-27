class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        print(f"{self.__class__.__name__}: I am printing")

    def fax(self, document):
        print(f"{self.__class__.__name__}: I am sending/receiving fax.")

    def scan(self, document):
        print(f"{self.__class__.__name__}: I am scanning.")


class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f"{self.__class__.__name__}: I am printing")

    def fax(self, document):
        """Not supported"""
        pass   # not in use but exists

    def scan(self, document):
        """Not supported"""
        pass   # not in use but exists


# some methods of the Machine class are not used, which is an issue - we have redundant methods that do nothing

doc = "Doc"

multi_printer = MultiFunctionPrinter()
multi_printer.print(doc)
multi_printer.fax(doc)
multi_printer.scan(doc)

old_printer = OldFashionedPrinter()
old_printer.print(doc)
old_printer.fax(doc)  # not in use but exists
old_printer.scan(doc)  # not in use but exists
