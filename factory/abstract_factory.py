from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):  # used to mandate a particular API
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious.")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious.")


# FACTORY
class HotDrinkFactory(ABC):
    def prepare(self, amount: int):  # used to mandate a particular API
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print(f'Preparing tea {amount} ml.')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print(f'Preparing coffee {amount} ml.')
        return Coffee()


# naive approach - w/o using abstract classes functionality
def make_drink(drink_type: str):
    if drink_type == "tea":
        return TeaFactory().prepare(200)
    elif drink_type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None


# abstract factory approach
class AvailableDrink(Enum):
    TEA = auto()
    COFFEE = auto()


# FACTORY
class HotDrinkMachine:
    factories = []  # [(name, instance), ...]
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in AvailableDrink:
                name = d.name[0] + d.name[1:].lower()  # get drink name out of Enum
                factory_instance = eval(name + "Factory")()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for id, f in enumerate(self.factories):
            print(f'>>> {f[0]} - {id}')  # print name of all drinks

        entry = input(f'Please pick a drink (0-{len(self.factories)-1}):\n')
        drink_id = int(entry)

        if drink_id not in range(0, len(self.factories)):
            print(f"Drink with id {drink_id} is not available.")
            return

        entry = input(f'Specify amount:\n')
        amount = int(entry)
        return self.factories[drink_id][1].prepare(amount)

# abstract factory approach uses hierarchy of factories
# execution chain: HotDrinkMachine.factories -> HotDrinkFactory.prepare()
# abstract classes used to mandate a particular API (can be omitted because of the Python duck typing)


if __name__ == "__main__":
    # naive approach
    def naive_approach():
        entry = input('What kind of drink would you like?\n')
        drink = make_drink(entry)
        drink.consume() if drink else print('This drink is not available.')

    # abstract factories approach
    def abstract_class_approach():
        hd_machine = HotDrinkMachine()
        drink = hd_machine.make_drink()
        drink.consume()

    # naive_approach()
    abstract_class_approach()
