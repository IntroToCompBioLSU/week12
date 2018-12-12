#!/usr/bin/env python

while True:
   try:
      int = int(input("Please enter a number: "))
      break
   except ValueError:
      print("That was not a number, don't worry, everyone makes typos. Please try again. ")

# DB: Nice example! One thing: it's best not to use 'int' as a variable name.

"""while True:
            try:
                myWord = input("Enter a word with five letters: ")
                assert len(myWord) == 5
                break
            except AssertionError:
                print("You didn't enter a word with five letters!")"""
