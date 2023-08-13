#A class method is a method that is bound to the class and not the object of the class
class emp:
    company="apple"
    def show(self):
        print(f"{self.company} has emp {self.name}")
    
    @classmethod # with the use of this decorator we can change class variables 
    def changecompany(cls,newName): # the 1st arg is always consider as self and it will add object to it we can write any name for it
        cls.company=newName

e1=emp()
e1.name="danish"
e1.changecompany("tesla") # it will add compant to instance
e1.show()

print(emp.company)

