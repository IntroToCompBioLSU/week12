#!/usr/bin/env python	# DB: Need shebang at top.

class sequence:		# DB: This class called "sequence" throughout rest of code.
            """A class to store information about any sequences in reference genomic data."""

            def __init__(self, group="Genome", doubleStranded=False):
                self.group = group
                self.doubleStranded = doubleStranded

            def summarize(self):
                if (self.doubleStranded):
                    print("This sequence is double stranded  and is a member of the %s." % (self.group))
                else:
                    print("This sequence is not double stranded  and is a member of the %s" % (self.group))


class dna(sequence):	# DB: Small indentation error.
            """
            A class to store information about sequences that are dna.
            The base class is sequence.
            """

            def __init__(self, length="", shortRead=True):
                sequence.__init__(self)  # Call base class constructor
                self.length = length

            def notAshortRead(self):
                self.shortRead = True
                print("%s is considered a dna, short read fragment." % (self.name))

#create a new dna 
dna1 = dna(length="6bp",shortRead=False)	# DB: Forgot '=' after length, also need t in shortRead

dna1.summarize()


class rna(sequence):
            """
            A class to store information about sequences that are dna.
            The base class is sequence.
            """

            def __init__(self, length="", shortRead=True):
                sequence.__init__(self)  # Call base class constructor
                self.length = length

            def notAshortRead(self):
                self.shortRead = True
                print("%s is considered a rna, short read fragment." % (self.name))

#create a new rna 
rna1 = dna(length="9bp",shortRead=False)	# DB: Forgot '=' after length, also need t in shortRead

rna1.summarize()


class protein(sequence):
            """
            A class to store information about sequences that are dna.
            The base class is sequence.
            """

            def __init__(self, length="", shortRead=True):
                sequence.__init__(self)  # Call base class constructor
                self.length = length

            def notAshortRead(self):
                self.shortRead = True
                print("%s is considered a protein, short read fragment." % (self.name))


#create a new protein. 
pro1 = dna(length="12bp",shortRead=False)	# DB: Forgot '=' after length, also need t in shortRead

pro1.summarize()

# DB: Good, I like this example. But several small syntax errors throughout.