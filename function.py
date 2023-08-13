# for reusablility we uses functions .

# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# we can wrap the code which we have to resuse in a function and use it where we want by calling it .

# functions are 2 types:
# built in
# user-defined

# there are 4 type of arguements which we can provide to the function:
# default
# keyword
# required argurements
# variable length arguements


# def average(a,b):
#     c=(a+b)/2
#     print (c)


# average(10,10)

def isgreat(a,b):
    if(a>b):
        print("1st no is greater")
    else:
        print("2nd no is greater")

# isgreat(1,2)

def name(a):
    pass  # pass means continues other program as the body of function will be defined later

# syntax of function 

# def func_name():
#     body


def name(a="danish"):
    print(a)

# name("kartik") # these are default arguements

def helo(a,b="kalua"):
    print(a,b)

# helo(a="danish ") #we must have to pass the value of a 

def tup(*a):   # with the use of * it will take arguement as tuple
    print(type(a))

# tup(2)

def dict(**ba):  # with the use of ** it will take arguement as dictionary
    print(type(ba))

# dict()

# return function is used to return the value back to the calling function
def num(a):
    return(a) # this return method will provides the value of a to baba keyword where we have used it 

baba=num(10) 
print(baba)