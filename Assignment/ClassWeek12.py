#!/usr/bin/env python

#class that contains generic information
class Car:
	"""This is a class to store information about any type of Car"""
	def __init__(self, Type=" ", Model=""):
		self.Type = Type
		self.Model = Mdel

	def summarize(self):
		if (self.Model) == "SUV":
			print("This Car is Low on MPG.")
		else:
			print("This Car has Average/Good MPG.")
class Brand(Car):

	"""This is a class used to store information on what brand the car is."""

	def __init__(self, Brand=" ", Model="SUV", Size="Large Vehicle"):
		clothes.__init__(self)
		self.Brand = Brand
		self.Model = Model
		self.Size = Size
	def summarize(self):
		Car.summarize(self)
		print("This Car is a %s, %s from the brand %s." %( self.Size, self.Model, self.Brand))
#Class that shares properties with the car.
class Cost(car):

        """This is a class used to store information on Cost of Cars"""

        def __init__(self, Cost=" ", Model="SUV", Size="Large Vehicle"):
                clothes.__init__(self)
                self.Cost = Cost
                self.Size = Size
        def summarize(self):
                Car.summarize(self) #summarizes all properties of the car
                print("This Car is a %s %s and cost %s." %( self.Size, self.Model, self.Cost))

#defining the items in the class
CarOne = Brand(Brand="Chevy", Size="Large", Model="SUV",)
CarOne = Cost(Cost="Expensive")
