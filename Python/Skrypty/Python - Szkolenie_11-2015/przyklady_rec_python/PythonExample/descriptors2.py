class MyClass(object):
    @property
    def x(self):
        return self.__x
    @x.getter 
    def x(self):
        print "Pobranie atrybutu x"
        return self.__x
    @x.setter
    def x(self, value):
        print "Ustawienie x na", value
        self.__x = value
    @x.deleter
    def x(self):
        print "Usuniecie x"
        del self.__x

a = MyClass()
a.x = 999
w = a.x
del a.x
