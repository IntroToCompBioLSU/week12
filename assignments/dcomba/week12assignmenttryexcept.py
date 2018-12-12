#!/usr/bin/env python

try:
      mySeq = input("Enter a DNA sequence: ")
      assert (mySeq.count("U") == 0)
except:
      print("You entered RNA rather than DNA!")

# DB: Great!