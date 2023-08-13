#Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class
# greet will take a function and it will run good moring befoer calling the function adn thanks a lot after calling the function
# it will take a function as an arguement and it will return it after modifying it

def greet(fx):
    def mfx(*args,**kwargs):     # args and kwargs means that if it takes arguements then take them
         print("good morning")
         fx(*args,**kwargs)
         print("thanks a lot")
    return mfx

@greet
def add(a,b):
     print(a+b)

@greet
def helo():
     print("hi bro")

add(1,2)
helo()
#greet(hello)() this will work same as @greet
# greet(add)(2,3)