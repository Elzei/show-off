#!/usr/bin/env python2.7

print "Before decorator definition"

def decorator(function):
    """Decorator"""
    print "Before decoration"
    def wrapper(*args, **kwargs):
        """Wrapper"""
        print "In wrapper"
        answer = function(*args, **kwargs)
        print "After wrapper"
        return answer
    print "After decoration"
    return wrapper

print "After decorator definition"

@decorator
def calculate(a, b, c):
    return a * 2 + b * 3 + c

if __name__ == '__main__':
    calculate(2, 3, 4)

# OUT:
#Before decorator definition
#After decorator definition
#Before decoration
#After decoration
#In wrapper
#After wrapper
