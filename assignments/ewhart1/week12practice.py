#!/usr/bin/env python

class clothes:
	"""A class for the overarching definition of clothes"""

	def __init__(self, brand="Adidas", material=""):
		self.brand = brand
		self.material = material

	def summarize(self):
		if (self.material):
			print("This item is made of %s" % self.material) #insert a material (leather, mesh, etc...)
			# DB: Need to finish insertion of material into string above.

class shoes(clothes):
	"""This class is a subset of clothes and contains adidas shoes?"""

	def __init__(self, color="", price="overpriced", size=""):
		clothes.__init__(self) #call base clothes constructor
		self.color = color
		self.price = price
		self.size = size
		
	def summarize(self):
		clothes.summarize(self)	# DB: this needs to call the clothes summarize function
		print("Congrats, you have just purchased a pair of %s" % self.brand)

purchase = shoes(size="12", color="white", price="overpriced")
purchase.summarize()

# DB: Overall, good! Need to be consistent in style of indentation (tabs or spaces.). 
#     All methods for a given class need to be indented the same amount. A few other minor
#     errors.