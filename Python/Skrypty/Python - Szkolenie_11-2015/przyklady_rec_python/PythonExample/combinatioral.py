#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import mul, add, truth

# TODO: Poprawić na wersję funkcyjną
def apply_each(fns, args=[]):
    for i in fns:
        args = map(i, args)
    return args

bools = lambda lst: map(truth, lst)

bool_each = lambda fns, args=[]: bools(apply_each(fns, args))

conjoin = lambda fns, args=[]: reduce(mul, bool_each(fns, args))

all = lambda fns: lambda arg, fns=fns: conjoin(fns,(arg, ))

both = lambda f, g: all((f,g))

all3 = lambda f, g, h: all((f,g,h))

and_ = lambda f, g: lambda x, f=f, g=g: f(x) and g(x)

disjoin = lambda fns, args=[]: reduce(add, bool_each(fns, args))

some = lambda fns: lambda arg, fns=fns: disjoin(fns, (arg,))

either = lambda f, g: some((f,g))

anyof3 = lambda f, g, h: some((f,g,h))

compose = lambda f, g: lambda x, f=f, g=g: f(g(x))

compose3 = lambda f, g, h: lambda x, f=f, g=g, h=h: f(g(h(x)))

ident = lambda x: x

if __name__ == '__main__':
    f1 = lambda x: x*3
    f2 = lambda x: x+3
    print apl(f1,[1,2,3,4])
    
