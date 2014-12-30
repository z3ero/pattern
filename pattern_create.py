#!/usr/bin/python3


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


import sys
import argparse
from itertools import islice, cycle

from pattern import *


def main(argv=None):
    argparser = argparse.ArgumentParser()
    argparser.add_argument('length', type=int)
    argparser.add_argument('sets', nargs='*', default=DEFAULT_PATTERN_SETS)
    argparser.add_argument('-a', '--alignment', type=int, default=None)
    argparser.add_argument('-f', '--allow-repeats', action='store_true')
    if argv is None:
        args = argparser.parse_args()
    else:
        args = argparser.parse_args(argv)

    try:
        print(''.join(pattern_create(args.length, args.sets, args.alignment,
                                     args.allow_repeats)))
    except NotEnoughPermutationsError as e:
        print(e, file=sys.stderr)
        print('(use -f to ignore)', file=sys.stderr)
        return 2
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
