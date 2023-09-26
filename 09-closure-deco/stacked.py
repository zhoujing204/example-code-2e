print("Runtime starts:")

def first(f): # <2> The first decorator function
    print('@first running at import time.')
    print(f'apply first({f.__name__})')

    def inner1st(n): # <4> The first decorator function
        result = f(n)
        print(f'inner1({n}): called {f.__name__}({n}) -> {result}')
        return result
    return inner1st


def second(f): # <1> The second decorator function
    print('@second running at import time.')
    print(f'apply second({f.__name__})')

    def inner2nd(n): # <3> The second inner decorator function
        result = f(n)
        print(f'inner2({n}): called {f.__name__}({n}) -> {result}')
        return result
    return inner2nd


@first
@second
def double(n):   # <5> The decorated function
    return n * 2

print("Before print double(3)")
print(double(3))

# Functions execution sequence:
# <1> The second decorator function
# <2> The first decorator function
# <3> The second decorator inner function
# <4> The first decorator inner function
# <5> The decorated function
# All the decorator functions(outer and inner) don't
# need to be invoked explicitly.
# The decorated function need to be invoked explicitly.





# def double_(n):
#     return n * 2


# double_ = first(second(double_))

# print(double_(3))
