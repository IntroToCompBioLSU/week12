#!/usr/bin/env python	# DB /usr/bin/, rather than /bin/usr/

while True:
    try:
        x = int(input("Enter a number: "))
        break
    # if the value is not an integer
    except ValueError:
    	print("That was not a valid number.  Try again...")
    	
# DB: Good!