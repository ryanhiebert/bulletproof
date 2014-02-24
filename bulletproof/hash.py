import collections.abc

class Hash(collections.abc.Mapping, collections.abc.Hashable):
    """A persistent, immutable, dictionary"""

    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            return TypeError(
                '{} expected at most {} arguments, got {}'.format(
                    type(self), 1, len(args)))
        self.__dict = dict(*args, **kwargs)
        for val in self.__dict.values():
            if not isinstance(val, collections.abc.Hashable):
                raise TypeError(
                    "unhashable type: {}".format(type(val)))

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, repr(self.__dict))

    __str__ = __repr__

    def __getitem__(self, item):
        return self.__dict[item]

    def __iter__(self):
        return iter(self.__dict)

    def __len__(self):
        return len(self.__dict)

    def __hash__(self):
        return hash(frozenset(__dict.items()))

    def __eq__(self, other):
        return self.__dict == dict(other)

    def __add__(self, other):
        if not other:
            return self
        copy = self.__dict.copy()
        copy.update(type(self)(other).__dict)
        return type(self)(copy)

    __radd__ = __iadd__ = __add__

    def remove(self, *keys):
        """Returns a new Hash, with the given key(s) removed"""
        copy = self.__dict.copy()
        for key in keys:
            copy.pop(key, None)
        return type(self)(copy)
