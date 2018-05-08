import datetime as dt


def add(a, b):
    return a + b


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


def non_return(x):
    x = x*x
    return x


x = float(input("->"))
print(non_return(x))
