#!/usr/bin/env python

#user has chosen from a list of numbered options for proceeding with script.
#user will be asked whether they have made the correct choice.
try:
	Answer = (input("Enter an yes or no:  "))
	assert len(Answer) == 3

#if the input is not a three letter word: yes
except AssertionError:
	print("You have answered no. Proceeding further requires the user to answer yes. Program is now ending.")
