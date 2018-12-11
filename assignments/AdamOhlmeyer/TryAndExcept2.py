#!/usr/bin/env python

#second Try and Except. Can't divide a number by 0.

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)