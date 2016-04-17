# -*- coding: utf-8 -*-
import time
from solve import *


def test_smart_decorator():
    # Нужно написать декоратор decorator_inc, который можно вызывать
    # как с аргументами, так и без. Декоратор инкрементирует
    # значение, которое возвращает функция. По умолчанию на 1
    # или на значение которое передается аргументом.

    @decorator_inc
    def foo():
        return 1

    @decorator_inc(2)
    def boo():
        return 1

    assert foo() == 2
    assert boo() == 3


def test_capture_decorator():
    # Реализовать декоратор decorator_capture, который принимает
    # список, в котором копятся аргументы, переданные
    # в декорируемую функцию.

    capture = []

    @decorator_capture(capture)
    def foo(boo, bar=None, **baz):
        return boo + (bar or 0) + sum(baz.values())

    assert foo(1, bar=2, baz=10) == 13
    assert foo(1, 20) == 21
    assert foo(1, baz=10) == 11

    assert capture == [{'baz': 10, 'bar': 2, 'boo': 1},
                       {'bar': 20, 'boo': 1},
                       {'baz': 10, 'bar': None, 'boo': 1}]


def test_timing_decorator():
    # Реализовать декоратор decorator_time, который замеряет время
    # выполнения функции и возвращает его в паре с результатом

    @decorator_time
    def foo(arg, ms):
        time.sleep(ms / 1000.0)
        return arg

    @decorator_time
    def bar(arg1, arg2, ms):
        time.sleep(ms / 1000.0)
        return arg1 + arg2

    result, duration = foo(10, 100)
    assert result == 10
    assert 0.07 < duration < 0.13

    result, duration = bar(1, arg2=2, ms=200)
    assert result == 3
    assert 0.17 < duration < 0.23


def test_mimic_decorator():
    # Написать декоратор decorator_mimic, который прикидывается
    # декорируемой функцией

    def foo(arg):
        return arg

    foo.attribute = 'boo'
    foo = decorator_mimic(foo)

    assert foo.__name__ == 'foo'
    assert foo.attribute == 'boo'
    assert foo(42) == 42

    def bar(a, b):
        return a + b

    bar.attribute = 'baz'
    bar = decorator_mimic(bar)

    assert bar.__name__ == 'bar'
    assert bar.attribute == 'baz'
    assert bar(1, 2) == 3
