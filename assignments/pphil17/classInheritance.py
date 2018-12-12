#!/usr/bin/env python

Class sports:
    """A class to store information about sports."""

	# DB: Some indentation errors in this definition.

    def init(self, group = "hobby", olympicSport=True):
		self.group = group
		self.olympicSports = olympicSports

	def summerize(self):
		if self.olympicSport:
		   print("This sport is an Olympic sport, and is a %s." % (self.group))
		else:
		   print("This sport is not an Olympic sport, but is a %s." % (self.group))

class ball(sports):
    """A class to store information about sports that use balls."""

    def init(self, name="", ball=False):
       self.name = name
       self.ball = ball

    def summarize(self):
       if (self.ball):
          print("%s is a sport that uses a ball.")
       else:
          print("%s is a sport that does not use a ball.")

# DB: Looks good! Did you attempt a try...except block?