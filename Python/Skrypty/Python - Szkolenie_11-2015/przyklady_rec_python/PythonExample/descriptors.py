class MyDescriptor(object):
    def __init__(self, initVal=None):
        self.__initVal = initVal
    def __get__(self, inst, typ):
        print "Dostep z obiektu", inst, "\n typu", typ
        return self.__initVal
    def __set__(self, inst, value):
        print "Ustawienie w obiekcie", inst, "\n wartosc", value
        self.__initVal = value
    def __delete__(self, inst):
        print "Usuniecie z obiektu", inst
        del self.__initVal

class MyClass(object):
    x = MyDescriptor(12)

a = MyClass()
w = a.x
a.x = 333
del a.x
