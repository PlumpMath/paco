# -*- coding: utf-8 -*-
import pytest
import asyncio
from paco.assertions import (assert_corofunction,
                             assert_iter, isiter,
                             iscoro_or_corofunc,
                             iscallable, isfunc)


def test_isiter():
    assert isiter(())
    assert isiter([])
    assert not isiter('foo')
    assert not isiter(bytes())
    assert not isiter(True)


def test_iscallable():
    @asyncio.coroutine
    def coro():
        pass

    assert iscallable(test_iscallable)
    assert iscallable(lambda: True)
    assert iscallable(coro)
    assert not iscallable(tuple())
    assert not iscallable([])
    assert not iscallable('foo')
    assert not iscallable(bytes())
    assert not iscallable(True)


def test_isfunc():
    @asyncio.coroutine
    def coro():
        pass

    assert isfunc(test_isfunc)
    assert isfunc(lambda: True)
    assert not isfunc(coro)
    assert not isfunc(tuple())
    assert not isfunc([])
    assert not isfunc('foo')
    assert not isfunc(bytes())
    assert not isfunc(True)


@asyncio.coroutine
def coro(*args, **kw):
    return args, kw


def test_iscoro_or_():
    assert iscoro_or_corofunc(coro)
    assert iscoro_or_corofunc(coro())
    assert not iscoro_or_corofunc(lambda: True)
    assert not iscoro_or_corofunc(None)
    assert not iscoro_or_corofunc(1)
    assert not iscoro_or_corofunc(True)


def test_assert_corofunction():
    assert_corofunction(coro=coro)

    with pytest.raises(TypeError, message='coro must be a coroutine function'):
        assert_corofunction(coro=None)


def test_assert_iter():
    assert_iter(iterable=())

    with pytest.raises(TypeError, message='iterable must be an iterable'):
        assert_iter(iterable=None)
