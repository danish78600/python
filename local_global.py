# the variables whihc are not accessabel outisde func - local
# function inside in local from outside - global
# local varibles are destroyed when function is finished
# global and local varible works differently

x=4
def d():
    
    y=10
    global x  # this will change the global value of x
    x=5
    print(x)

d()
print("global x is", x)
# print(y) # this will throw an error as  x is local variabkle and cannot be accesed oudside we can access it by global variable