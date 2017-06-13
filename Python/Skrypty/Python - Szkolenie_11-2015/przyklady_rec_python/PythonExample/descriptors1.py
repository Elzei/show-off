class MyClass(object):
    def get_x(self):
        print "Dostep do x"
        return self.__x
    def set_x(self, value):
        print "Ustawienie x na", value
        self.__x = value
    def del_x(self):
        print "Usuniecie x"
        del self.__x
    x = property(get_x, set_x, del_x, "Attr. x")

a = MyClass()
a.x = 999
w = a.x
del a.x
