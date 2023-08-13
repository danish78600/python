# python do not have public private protected keywords but are discused
# public - members are accessible from outside the class. private - members cannot be accessed (or viewed) from outside the class. protected - members cannot be accessed from outside the class, however, they can be accessed in inherited classes. 
# access modifiers are used to restrict the access of the class member variable and methods from outside the class

class emp:
    def __init__(self):
        self.__name="danish"

a=emp()
# print(a.__name)  # so it is a private var so cannot be directly accessed
print(a._emp__name) # private var can be accessed with this code
print(a.__dir__())  # print all the built in methods

# when we make a variable is prefix with __ then it is a weak indication of private variable but we can access it 
#In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class
# but with inheritence we can access the base class private methods directly