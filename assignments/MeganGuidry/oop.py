#!/usr/bin/env python

class clothes:
    """A class to store information about items of clothing."""

    def __init__(self, size="", color=""):
        self.size = size
        self.color = color
    def summarize(self): 
        if self.size == "M":
            print("This item is a size medium and item color is %s." % self.color)
        else: 
            print("This item is not size medium. Item size: %s. Item color: %s." % self.size % self.color)

sock= clothes(size="S", color="blue")
sock.summarize

class shirt(clothes):
    """A class to store information about shirts. Base class is clothes."""

    def __init__(self, sleeves="short", size="", color="red"):
        clothes.__init__(self, size="M", color= "red")
        self.sleeves= sleeves
    def summarize(self):
        clothes.summarize(self)
        print("This item of clothing is a shirt. It has %s sleeves." % self.sleeves)

tshirt= shirt(size="S", color="blue", sleeves="3/4")
tshirt.summarize()

# DB: Great example!