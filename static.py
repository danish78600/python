# the objects which not belong to insatnce of a class

#static methods are made within the class without using self as we can also declare it outside class but we have declared it inside class as the person who will use calss can acces it
# these static methods can also be called independently as it is not associated with class

class adding:
    def __init__(self,num):
        self.num=num

    def additional(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a + b
    
a=adding(9)
print(a.num)
a.additional(10)
print(a.num)

# print(a.add(1,2))
print(adding.add(1,2)) # we can also call it by class name

