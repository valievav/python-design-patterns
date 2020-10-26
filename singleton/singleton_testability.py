import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# target class that uses Singleton as metaclass
class Database(metaclass=Singleton):
    """
    Return capitals - their population.
    """
    def __init__(self):
        self.population = {}

        with open('capitals.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            for i in range(0, len(lines), 2):
                self.population[lines[i]] = int(lines[i+1])


class RecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.db.population[city]
        return result


# db with test data for unit tests
class DummyDatabase:
    population = {
        "Bristol": 120000,
        "Dulf": 150000,
        "Senth": 45000
    }


class SingletonTest(unittest.TestCase):

    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        db = DummyDatabase()
        rf = RecordFinder(db)
        self.assertEqual(120000+150000, rf.total_population(['Bristol', 'Dulf']))


if __name__ == "__main__":
    unittest.main()
