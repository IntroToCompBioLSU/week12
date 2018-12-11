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

    def __init(self, name="", leisure=False):
        sports.__init__(self)
        self.name = name
        self.leisure = leisure

    def summarize(self):
        sports.summarize(self)
        print("This is a leisure activity.")
        print