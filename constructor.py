#constructors are used for creting objects of a class and initialsing methods and variables to them
#2 types- parametrised,default
#when the constructor donot have any arguements without self which is automatic then it is default

class state:
    # capital="amitsar"
    # debt="20lakh"

    # the below is a constructor and is also called dunder method and it is always be invoked when object is created
    # so to take its benifits we cna assign value to variable always in the object for constructor when it is called
    def __init__(self,c,d): # the 1st param self is automatically passed which is object
        self.capital=c
        self.debt=d
       

    def info(self):
        print(f"{self.capital} has taken debt of {self.debt}")

a=state("asr","20crore")   
a.info()

# the above is more convienient code than the below 
# The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes


# a.capital="chandigarh"
# a.info()