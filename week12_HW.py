#!/usr/bin/env python

class cars:
   """A class to store information about any kind of car"""

   def __init__(self, size="", color=""):
      self.size = size
      self.color = color

   def summarize(self):
      if self.size == "S":
         print("This car is small and it's color is %s." % self.color)
      else:
         print("This car is not small. It's color is: %s." % self.color)

class SUV(cars):
   """A class to store information about SUV's. Base class is cars."""

   def __init__(self, size="", color="blue"):
      cars.__init__(self, size="S", color= "blue")

   def summarize(self):
      cars.summarize(self)
      print("This car is an SUV. It is %s." % self.color)

vehicle= cars(size="L", color="blue")
vehicle.summarize()

