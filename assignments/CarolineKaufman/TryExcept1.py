#!/bin/usr/env python

while True:
    try:
        x = int(input("Enter a number: "))
        break
    # if the value is not an integer
    except ValueError:
    	print("That was not a valid number.  Try again...")