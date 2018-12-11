#!/usr/bin/env python

#Line:1, parent class 
class Person:  
    #variables  
    name = ""  
    age = 0  
  
    #constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
#end parent class definition

class Student(Person): 
	#this is the sub class 
    studentId = ""  
    def __init__(self, studentName, studentAge, studentId):  
        Person.__init__(self, studentName, studentAge) 
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId 
         #returns the value of student id

#end of subclass definition

# Create an object of the parent class  
person1 = Person("Mom", 55) 

#show age of person 1 
person1.showName()
person1.showAge()  

# object for subclass

student1 = Student("Caroline", 23, "89-499-")  
print(student1.getId())  
student1.showName()  