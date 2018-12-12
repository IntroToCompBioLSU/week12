#!/usr/bin/python
class CellStuff:
    """a base class for intercellular molecules"""
    def __init__(self,kind="organic",essential=True):
        self.kind = kind
        self.essential = essential
    def summary(self): #summary function for Cell Stuff
            print("%s is %s stranded and made up of %s sugars \nand %s bases." % (self.name,self.strands,self.sugar,self.bases))
class nAcid (CellStuff):
    """Class for DNA"""
    def __init__(self,name="",strands="",sugar="",bases=""):
        CellStuff.__init__(self)
        self.name = name
        self.strands = strands
        self.sugar = sugar
        self.bases = bases

class pro (CellStuff):
    """docstring for protien"""
    def __init__(self,name="",strands="",):
        CellStuff.__init__(self)
        self.name = name
        self.stands = strands
    def summary(self): #modified summary for proteins
        print("A %s is an %s molecule that is translated from RNA." % (self.name,self.kind))

#adding objects to classes
rna = nAcid(name="RNA",strands="Double or Single",sugar="ribose",bases="Guanine,Uracil,Adenine,and Cytosine")
dna = nAcid(name="DNA",strands="Double",sugar="deoxyribose",bases="Guanine,Thymine,Adenine,and Cytosine")
protien = pro(name="Protien",strands="N/a" )

#Do Stuff
print("_____________________________________________________")
print("                 Summary of Classes")
print("_____________________________________________________")
dna.summary()
print()
rna.summary()
print()
protien.summary()

# DB: I really like these examples! Did you attempt a try...except block?