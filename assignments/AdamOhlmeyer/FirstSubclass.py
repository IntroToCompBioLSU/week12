#!/usr/bin/env python

#Defining a base class for all employees
class Employee:

#Setting the raise amount for employees
	raiseAmt = 1.05		# DB: Probably want this in the constructor.

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

#defining a method to apply the raise
	def applyRaise(self):
		self.pay = int(self.pay * self.raiseAmt)

#Defining a subclass for employees that are managers
class Manager(Employee):
	
	raiseAmt = 1.15		# DB: Probably want this in the constructor.

	def __init__(self, first, last, pay, favColor):
		Employee.__init__(self, first, last, pay)
		self.favColor = favColor



#Creating an employee
emp1 = Employee('John', 'Doe', 80000)

#creating a manager 
man1 = Manager('Dale', 'Earnhardt Sr.', 200000, 'black')

print(emp1.first, emp1.last)
print(emp1.pay)
print(man1.first, man1.last)
print(man1.pay)
print("The Intimidator's Pay After Raise:")
man1.applyRaise()
print(man1.pay)

# DB: Good!