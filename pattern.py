'''
This file is part of Pattern.

Pattern is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your
option) any later version.

Pattern is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with Pattern.  If not, see <http://www.gnu.org/licenses/>.
'''


import string
from fractions import gcd
from itertools import islice, cycle, chain, product
from functools import reduce
import operator


DEFAULT_PATTERN_SETS = [string.ascii_uppercase, string.ascii_lowercase,
                        string.digits]


def lcm(a, b):
    return a * b // gcd(a, b)


def weave(sets):
    if not sets:
        raise ValueError('no sets')
    union = set()
    for s in sets:
        sset = set(s)
        if len(sset) != len(s):
            raise ValueError('duplicate item in set')
        if not union.isdisjoint(sset):
            raise ValueError('intersecting sets')
        union |= sset

    return chain.from_iterable(product(*sets))


class NotEnoughPermutationsError(ValueError):
    def __init__(self, max_items):
        super(NotEnoughPermutationsError, self).__init__(
            'not enough permutations for more than {} items'.format(max_items))


def pattern_create(length=None, sets=DEFAULT_PATTERN_SETS, alignment=None,
                   allow_repeats=False):
    if length is not None and length < 0:
        raise ValueError('length cannot be negative')
    if alignment is not None and alignment < 0:
        raise ValueError('alignment cannot be negative')
    if length == 0:
        return []
    if alignment == 0:
        raise ValueError('alignment cannot be zero')

    num_unique_blocks = reduce(operator.mul, (len(s) for s in sets))
    unique_block_items = num_unique_blocks * len(sets)
    if alignment is None:
        max_items = unique_block_items
    else:
        max_items = lcm(unique_block_items, alignment)
    if length is None:
        length = max_items
    elif length > max_items and not allow_repeats:
        raise NotEnoughPermutationsError(max_items)

    return islice(cycle(weave(sets)), length)


__all__ = ['DEFAULT_PATTERN_SETS', 'weave', 'NotEnoughPermutationsError',
           'pattern_create']
