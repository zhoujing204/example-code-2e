"""
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__  # doctest: +ELLIPSIS
(<cell at 0x...: list object at 0x...>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

DEMO = """
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
"""


def make_averager():
    series = []
    
    # variable count is not referenced in the inner function, 
    # it's just a local variable, not a closure.
    count = len(series)    

    def averager(new_value):
        # series = [1, 2, 3]
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
