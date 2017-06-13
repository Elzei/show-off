# Bardzo podobny do singletona
class Borg(object):
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

if __name__ == '__main__':
    o1 = Borg()
    o1.x = 12
    o2 = Borg()
    o2.x = 13
    o3 = Borg()
    o3.x = 14
    # To sa inne obiekty!
    print o1, o2, o3
    # .. ale wspoldziela stan :)
    print o1.x, o2.x, o3.x

