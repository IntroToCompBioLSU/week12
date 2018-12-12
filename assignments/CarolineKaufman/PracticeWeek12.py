#!/usr/bin/env python

class clothes:  
     """A class to store information about any clothes"""
	def __init__(self, group="outerwear", warm=False):	# DB: Need to indent.
		self.group = group
		self.warm = warm

		def summarize(self):
			if (self.warm):
				print("These clothes are warm and is a member of the %s." % (self.group))
			else:
				print("These clothes are not warm and is a member of the %s" % (self.group))

class jackets(clothes):
      """
      A class to store information about clothes that are winter jackets.
      The base class is clothes.
      """
	def __init__(self, name="",winter=True):	# DB: Need to indent.
		clothes.__init__(self)  # Call base class constructor
		self.name = name
		self.winter = winter

	def heavy(self):
		self.winter = True
		print("%s is a winter jacket." % (self.name))

jackets.summary	# DB: There's no method with this name. Did you intend to override the
				# summarize() method of clothes?

#do color or sleeve legnth