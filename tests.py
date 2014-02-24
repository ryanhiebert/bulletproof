import collections.abc

import pytest
from bulletproof.hash import Hash

def test_instantiation():
    with pytest.raises(TypeError):
        Hash(5, 6)

    Hash(zip('abcd', 'efgh'))
    Hash({'a': 'e', 'b': 'f'})
    Hash(zip('abcd', 'efgh'), foo='spam', bar='eggs')
    Hash({'a': 'e', 'b': 'f'}, foo='spam', bar='eggs')

def test_repr():
    hash = Hash(zip('abcd', 'efgh'))
    assert hash == eval(repr(hash))
    assert repr(hash) == repr(eval(repr(hash)))

def test_unhashable():
    with pytest.raises(TypeError):
        Hash({5: []})

def test_subclass_repr():
    class MyHash(Hash):
        pass

    myhash = MyHash(zip('abcd', 'efgh'))
    assert myhash == eval(repr(myhash))
    assert repr(myhash) == repr(eval(repr(myhash)))

def test_getitem():
    hash = Hash({'a': 1, 'b': 2})
    assert hash['a'] == 1

def test_mapping():
    assert issubclass(Hash, collections.abc.Mapping)

def test_hashable():
    assert issubclass(Hash, collections.abc.Hashable)

def test_iter():
    assert frozenset(iter(Hash(zip('abcd', 'efgh')))) == frozenset('abcd')
