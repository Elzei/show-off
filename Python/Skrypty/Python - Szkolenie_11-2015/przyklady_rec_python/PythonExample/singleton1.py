def singleton(cls):
    instances = {}
    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getInstance

@singleton
class MySingleton(object):
    pass

if __name__ == '__main__':
    o1 = MySingleton()
    o2 = MySingleton()
    o3 = MySingleton()
    print o1, o2, o3

