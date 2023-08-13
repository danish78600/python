# the think which is same for all class is known as class varibales
#instance varibale are dfiiferent for different objects

class naming:
    cname="apple" #associated with class
    def __init__(self,name):
        self.name=name
        self.amt="0.2" # associated with instance
    def callit(self):
        print(f"the name of yours is {self.name}")
    def details(self):
        print(f"{self.cname} has amt {self.amt}")


danish=naming("danish")
# instance vairvbles are those that are associated with instance not with class
# both the below code are same
# when we call the 1st then it converts into 2nd 
# if we will remove self from above program then an error will come that you have given 1 arg and it takes nothing

danish.callit()
danish.amt=1.2 # it will cahnge as it is associated with instance
naming.cname="India" # if instance var is present then it will be shown otherwise class vatriable will be shown and if not then it will find a class var with same name.
danish.details()
# naming.callit(danish)

a=naming("dana")
a.callit()
a.details()


# Class variables are defined within the class but outside of any class methods. 
# Instance variables are defined within class methods, typically the constructor. 