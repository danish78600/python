# in python for error handling we use try except block
# An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions
# python has many built in exceptions
# in python we can throw multiple exceptions
# a=input("enter no")
# try:
#     for i in range(a):
#         print(a)

# except:
#     print("error occured")

# finally:
#     print("final block")

# final block - the code inisde it will print either error come or not
def func():
    try:
        l=[1,2,3,4]
        a=int(input())
        print(l[a])
        return 1
    except:
       return 0
    finally:
        print("final")

# func()

# in python we can raise custom exception errors by using the raise keyword 
a=int(input("enter value between 2 and 10"))
if(a<2 or a>10):
    raise ValueError("you have entered wrong no")
# value error is a built in error

#in python defining custom exceptions is done by creating a class that is derieved from built in functions