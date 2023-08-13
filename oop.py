# the programs which we are doing previosly was proceduural programming but now we have introduced to  object oriented programming
#Object-oriented programming (OOP) is a way of thinking about and organizing code for maximum reusability.
# If you had a class called “Expensive Cars,” it could contain objects like Mercedes, BMW, Toyota, and so on.

# in this firstly we will create a class  as it is a template(blueprint) for creating objects and we can crete multiple objects with the use of class
#oop map concepts to the real world entity

# example 

# reilway form-class
# harry- object created from class template
# tom - object created from class template

# objects are entity

# we can access the properties of object with the use of . operator
# features of oop

#. It describes the idea of wrapping data and the methods that work on data within one unit and can be accessed through object methods
# inheritence  allows us to define a class that inherits all the methods and properties from another class
# polymorphism means one think in multiple forms

#self is a reference that points to the current insatnce of class

class coder:
    lang="c++"
    sal="1000"
    def name(self):
        print(f"{self.sal} knows {self.lang}")

a=coder()
a.lang="c"
a.sal="20k"

# if we not make changes then it will take default values of the class
b=coder()
b.lang="python"
b.sal="10k"


# print(a.sal)
a.name() # self means name of the object for which the method is called
b.name()
