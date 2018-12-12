#!/usr/bin/env python


class car:
    """This is a class to define a car"""

    def __init__(self, doors, drive, make, model):
        self.doors = doors
        self.drive = drive
        self.make = make
        self.model = model

    def summarize(self):
        print("This car is a %s %s." % (self.make, self.model))


class sportsCar(car):
    """
    A class to store information about cars that are sport vehicles.
    The base class is cars.
    """

    # Call base class constructor
    def __init__(self, horsepower, zerotosixty, doors, drive, make, model):
        car.__init__(self, doors, drive, make, model)
        self.horsepower = horsepower
        self.zerotosixty = zerotosixty

    def summarize(self):
        car.summarize(self)
        print("It is a sports car with %d horsepower." % (self.horsepower))


myJeep = car(2,"rear","Jeep","Wrangler")
myBmw = sportsCar(200, 5.5, 2, "rear", "BMW", "328ci")

myJeep.summarize()
print("-------------")
myBmw.summarize()

# DB: Great example! I really like this.