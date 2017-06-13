def show(arg):
    print arg
    return arg + 1

if __name__ == '__main__':
    data = [ 10, 20, 30, 40 ]
    result = map(show, data)
    print "-" * 10
    print result
    print "-" * 10
    result = map(lambda x : x * 2 + 1, data)
    print result

