class myclass:
    def __init__ (self,value):
        self._value=value
    def show(self):
        print(f"the value is {self._value}")

    @property # this decorator property is used to make a getter method
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter #this decorator will work as a setter
    def ten_value(self,new_value):
        self._value=new_value/10
    

a=myclass(10)
# a.ten_value=10 this will throw an error as this is not a convinient way to set the value
a.ten_value=100 #in this code we are setting the value
print(a.ten_value) # in this we are getting the value
a.show()

#getters are the methods that is used to access the value of an object property
# property decorator works as a getter