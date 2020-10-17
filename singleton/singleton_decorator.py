def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Database:
    _instance = None

    def __init__(self):
        print('Loading db.')


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    # init run only once!
    print(d1 == d2)  # same obj
