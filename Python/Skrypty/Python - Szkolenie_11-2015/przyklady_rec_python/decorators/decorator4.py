#!/usr/bin/env python2.7

def decorator(function):
    """Decorator"""
    def wrapper(*args, **kwargs):
        """Wrapper"""
        answer = function(*args, **kwargs)
        return answer
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper

@decorator
def calculate(a, b, c):
    """ Calculate doc... """
    return a * 2 + b * 3 + c

if __name__ == '__main__':
    calculate(2, 3, 4)

    # No i problemu nie ma :-) 
    print calculate.__doc__
    print calculate.__name__
