#!/usr/bin/env python
class cars:
    """This class shows attributes of some cars"""
    def __init__(self,color="red"): 
        self.color=color
        
    def hotcake(self):
        if self.color is "red":
            print ("This car is a hotcake")
        elif self.color is "blue":
            print ("This car is not a hotcake")
        else:
            print("This is not even a car")
class  vans(cars):          
    """This class has information on vans only"""
    def __init__(self,sellingprice):
        cars.__init__(self)
        self.sellingprice=sellingprice
    def hotcake(self):
        cars.hotcake(self)
        if self.sellingprice is 100:
            print("This van is cheap")
        else:
            print("This van is expensive")
class trucks(cars):
    def __init__(self,color,make):
        """This class shows attributes in trucks"""
        cars.__init__(self,color)
        self.color=color
        self.make=make
    def new(self):
        cars.hotcake(self)
        if self.make is "chevy":
            print("This truck is great")
        else:
            print("This truck is wacky")
gue=vans(200)
gue.hotcake()
gud=trucks("blue","merc")
gud.new()

# DB: Good!