#!/usr/bin/env python

class clothes:
	"""A class for the overarching definition of clothes"""

	def __init__(self, brand="Adidas", material=""):
	    self.brand = brand
	    self.material = material

	    def summarize(self):
	    	if (self.material):
	    	    print("This item is a %d") #insert a material (leather, mesh, etc...)

class shoes(clothes):
	"""This class is a subset of clothes and contains adidas shoes?"""

	def __init__(self, color="", price="overpriced", size=""):
		clothes.__init__(self) #call base clothes constructor
		self.color = color
		self.price = price
		self.size = size
	def summarize(self):
		shoes.summarize(self)
		print("Congrats, you have just purchased a pair of %s" % self.brand)

purchase = shoes(size="12", color="white", price="overpriced")
purchase.summarize()
