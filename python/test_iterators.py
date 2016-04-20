# -*- coding: utf-8 -*-
# https://docs.python.org/2.7/tutorial/classes.html#iterators
# https://docs.python.org/2.7/tutorial/classes.html#generators
# https://docs.python.org/2.7/tutorial/classes.html#generator-expressions

import itertools
from solve import *


def test_random_iterator():
    # Реализовать random_iterator(), который возвращает случайные числа
    # от 0 до 1.

    count = 100000
    s = sum(itertools.islice(random_iterator(), count))
    estimate = count / 2
    assert estimate * 0.9 < s < estimate * 1.1


def test_sample_iterator():
    # Реализовать sample_iterator(seq, N) который выбирает
    # каждый Nый элемент из seq

    seq = itertools.count(1)
    result = list(itertools.islice(sample_iterator(seq, 7), 100))
    expect = [7*r for r in xrange(1, 101)]
    assert result == expect


def test_pair_iterator():
    # Реализовать pair_iterator(seq) который выбирает
    # пары из seq

    seq = itertools.count()
    result = list(itertools.islice(pair_iterator(seq), 100))
    assert result == [(r*2, r*2+1) for r in xrange(100)]


def test_group_iterator():
    # Реализовать group_iterator(seq) который схлопывает
    # одинаковые подряд идущие элементы в пары, (el, count)

    seq = itertools.chain.from_iterable([r]*r for r in itertools.count())
    result = list(group_iterator(itertools.islice(seq, 100)))
    expected = [(r, r) for r in xrange(1, 14)] + [(14, 9)]
    assert result == expected
