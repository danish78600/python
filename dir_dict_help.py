# tehy make it easy for us to how clases resolves fuction adn executes it
# The dir() function returns all properties and methods of the specified object, without the values.
#dict will return all the set attributes of the class .
x=[10,21,10]
print(dir(x))  # we will get all the methods of list
print(x.__add__)

class danish:
    def __init__(self,name):
        self.name=name

a=danish("danishbhaiu")
print(a.__dict__)

print(help(a))  # it will tells us all the matter of class as it will give us help