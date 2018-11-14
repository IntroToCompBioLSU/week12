#!/usr/bin/env python
#short statement showing ValueError
try:
    i=int("s")
except ValueError:
    print ("could not convert data into an integer")
