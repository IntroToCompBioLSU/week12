#!/usr/bin/env python

class Cars:
    """A class to store information about any car."""
    def __init__(self, make, model):
        self.make = make
        self.model = model

    #Defining a method to show the make and model of any car
    def Show(self):
    	print(self.make, self.model)

car1 = Cars('Toyota', 'Rav4')

class Trucks(Cars):
	"""A class to store information about trucks that are cars."""
	def __init__(self, make, model, DriveType):
	    Cars.__init__(self, make, model)
	    self.DriveType = DriveType

    #Defining a method to display the drive type of trucks
    
	def DispDriveType(self):
		print("This truck is", self.DriveType)

truck1 = Trucks('Toyota', 'Tundra', '4WD')

truck1.Show()
truck1.DispDriveType()