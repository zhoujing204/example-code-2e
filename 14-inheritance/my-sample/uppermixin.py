# tag::UPPERCASE_MIXIN[]
import collections

def _upper(key):  # <1>
    try:
        return key.upper()
    except AttributeError:
        return key

class UpperCaseMixin:  # <2>
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))
# end::UPPERCASE_MIXIN[]

# tag::UPPERDICT[]
class UpperDict(UpperCaseMixin, collections.UserDict):  # <1>
    pass

class UpperCounter(UpperCaseMixin, collections.Counter):  # <2>
    """Specialized 'Counter' that uppercases string keys"""  # <3>
# end::UPPERDICT[]