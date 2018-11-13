#!/usr/bin/env python

class Car:   #parent class
    "Parent Class"
    def __init__(self, price):
        self.price = price
    def display(self):
        print ('Price = $',self.price) #how much the car costs
#end parent class 

class Category(Car):   #derived class
    "Derived class"
    def __init__(self, price, name):
        Car.__init__(self, price)
        self.name = name #type of car

    def disp_name(self):
        print ("vehicle = ", self.name)

#end derived class

obj = Category(1500, 'Toyota')
obj.disp_name()
obj.display()