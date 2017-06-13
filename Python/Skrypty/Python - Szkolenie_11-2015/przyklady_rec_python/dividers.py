#!/usr/bin/env python2.7

def dividers(value):
    answer = []
    for i in xrange(1, (value // 2 ) + 1):
        if (value % i) == 0:
            answer.append(i)
    return answer

def dividers2(value):
    return filter(lambda x: (value % x) == 0, xrange(1, (value // 2) + 1))

def dividers_gen(value):
    half_range = (value // 2) + 1
    for i in xrange(1, half_range):
        if (value % i) == 0:
            yield i

def dividers2_gen(value):
    half_range = (value // 2) + 1
    return (i for i in xrange(1, half_range) if (value % i) == 0)

def perfect(value):
    answer = []
    for i in xrange(2, value + 1):
        if i == reduce(lambda x, y: x + y, dividers_gen(i)):
            answer.append(i)
    return answer

def perfect2(value):
    return filter(lambda x: x == reduce(lambda x, y: x + y, dividers_gen(x)),
            xrange(2, value + 1)
            )

def perfect_gen(value):
    for i in xrange(2, value + 1):
        if i == reduce(lambda x, y: x + y, dividers_gen(i)):
            yield i

def perfect2_gen(value):
    return (i for i in xrange(2, value + 1) if i == reduce(lambda x, y: x + y, dividers_gen(i)))



if __name__ == '__main__':
    print dividers(1024)
    print dividers2(1024)
    print "-" * 10
    for i in dividers_gen(1024):
        print i, 
    print "\n", "-" * 10
    for i in dividers2_gen(1024):
        print i,
    print "\n", "-" * 10
    print perfect2(100)
    print "-" * 10
    for i in perfect_gen(9000):
        print i, 
    print "\n", "-" * 10
    for i in perfect2_gen(9000):
        print i, 
