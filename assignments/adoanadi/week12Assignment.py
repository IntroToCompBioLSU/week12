#!/usr/bin/env python

class sports:
    """A class to store information about sports"""
    
    def __init__(self, group="outdoor", ball=False):
        self.group = group
        self.ball = ball
        
    def summarize(self):
        if (self.ball):
            print("This sport requires the use of a ball and is an % sport." % (self.group))
        else:
            print("This sport does not require the use of a ball and is an % sport." % (self.group))

class leisure(sports):
    """A class to store information about leisure activities that are sports."""
    
    def __init__(self, name="", leisure=True):	# DB: Need 2nd __ around init -- also maybe set leisure to True in this case?
        sports.__init__(self)
        self.name = name
        self.leisure = leisure
        
    def summarize(self):
        sports.summarize(self)
        print("This is a leisure activity.")
        
# DB: Aside from a couple of minor formatting changes, this looks good! Here's the output
#     I get when using this code:
#
#     >>> myLeisureSport = leisure()
#     >>> myLeisureSport.summarize()
#     This sport does not require the use of a ball and is an outdoorport.
#     This is a leisure activity.
