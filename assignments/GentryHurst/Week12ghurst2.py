#!/usr/bin/env python

#class that contains generic information
class clothes:
	"""This is a class to store information about any item of clothing"""
	def __init__(self, type=" ", season=""):
		self.type = type
		self.season = season

	def summarize(self):
		if (self.season) == "summer":
			print("This item of clothing is worn during the summer.")
		else:
			print("This item of clothing is not worn during the summer.")
# a class (within the class of clothes) that contains more specific properties for the class clothing.
class shirt(clothes):

	"""This is a class used to store information about clothes that are shirts"""

	def __init__(self, color="yellow", brand=" ", season="summer", type="shirt"):
		clothes.__init__(self)
		self.color = color
		self.brand = brand
		self.season = season
		self.type = type
	def summarize(self):
		clothes.summarize(self)
		print("This item of clothing is a %s %s from the brand %s." %(self.color, self.type, self.brand))
#Class that shares properties with shirts.
class jacket(clothes):

        """This is a class used to store information about clothes that are jackets"""

        def __init__(self, color="Black", brand=" ", season="winter", type="jacket"):
                clothes.__init__(self)
                self.color = color
                self.brand = brand
                self.type = type
        def summarize(self):
                clothes.summarize(self) #summarizes all properties of the clothing item
                print("This item of clothing is a %s %s from the brand %s." %(self.color, self.type, self.brand))

#defining the items in the class
ItemOne = shirt(color="pink", brand="Gucci")
ItemTwo = jacket(color="black",brand="The North Face")
#run the program
print("What item of clothing would you like to look up?")
#try and except statment
while True:
	try:
		user = input()
		if user == "ItemOne":
			print("Item One: \n")
			print(ItemOne.summarize())
		elif user == "ItemTwo":
			print("ItemTwo: \n")
			print(ItemTwo.summarize())
		break
#if not the correct input error message is printed
	except AssertionError:
		print("You didn't enter a correct item number. Try \"ItemOne\"")

# DB: I like these examples a lot, although I wasn't able to throw an AssertionError. You
#     might need to add an assert statement for that.
