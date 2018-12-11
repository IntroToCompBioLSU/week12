#!/bin/usr/env python

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    #if it cannot find the file
    except OSError:
        print('cannot open', arg)
    # if is can find the file print number of lines
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
