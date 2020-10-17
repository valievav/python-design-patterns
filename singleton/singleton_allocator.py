class Database:
    _instance = None

    # works good for class w/o initializer
    # reason is that __init__ is called after __new__ always, in any case
    # but if we want to call __init__ only once, this won't work as it doesn't prevent more than 1 __init__ calls
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    print(d1 == d2)  # same obj
