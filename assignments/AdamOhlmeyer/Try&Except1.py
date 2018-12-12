#!/usr/bin/env python

import sys

try:
	#To try and open a file
    f = open('myfile.txt')
    #To try to read the line
    s = f.readline()
    #to try and convert string to interger
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    
# DB: Good!