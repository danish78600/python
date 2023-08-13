# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"{self.name} has id no {self.id}")

class programmer(emp):
    def lang(self,lang):
        print("the lang is python")

danish=emp("danish",109)
danish.show()

harry=programmer("danish",200)
harry.lang()