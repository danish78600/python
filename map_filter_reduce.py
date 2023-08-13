# to make updates to each item of an list we uses map
def cube(x):
    return x*x*x

l=[2,3,4,5,8,10]
newl=list(map(cube,l))  # the 1st param is that which function you want to apply and 2nd param is the list in whihc you want to make changes

# print(newl)

# filter is used to filter the elements
def even(x):
    if(x%2==0):
        return x
newl2=list(filter(even,l)) # the 1st param is that which function you want to apply and 2nd param is the list which you want to filer
# list is used to convert the filter object to list
# print(newl2)

#reduce is also same as above 2 but we have to import it
from functools import reduce
def sum(x,y):
    return x+y
add=reduce(sum,l)
print(add)

# reduce will first add 2 and 3 and then their result 5 will be added to 4 no and so on