# CLASS METHODS CAN BE USED AS ALTERNATE CONSTRUCTORS

class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    @classmethod # the code will work same as constructor but it will work with differnet data 
    #they are using class methods as alternative constructor
    def fromstr(cls,str):
        return cls(str.split("-")[0],str.split("-")[1])


# a=emp("danish",1000)
# print(a.name)

string="danish-1000"
a=emp.fromstr(string)
print(a.name)
print(a.sal)