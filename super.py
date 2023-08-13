# super keyword in python is used to represent the parent class 
# class danish:
#     def dana(self):
#         print("danish")

# class kartik(danish):
#     def new(self):
#         print("this is the super class methods")
#         # super().dana() # 

# a=kartik()
# a.dana() # it will first search the dana() in present class if not preesent then it will find it in super class

# using super for constructor
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id) # it will directly get the attributes of super class constructor
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)