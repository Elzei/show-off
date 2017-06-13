
class MyClass(object):
    def __init__(self, val):
        self._value = val

    @property
    def value(self):
        return self._value + 10

    @value.setter
    def value(self, val):
        self._value = val

    @value.deleter
    def value(self):
        print "Wow!... I'm delete!!"

if __name__ == '__main__':
    o = MyClass(100)
    print o.value
    o.value = 5000
    print o.value
    del o.value
