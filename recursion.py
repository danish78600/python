# in python function can call other functions. fucntion can call itself in python 

# factorial(7)=7*factorial(6)
# factorial(6)=6*factorial(5) and so on

# factorial(n)=n*factorial(n-1)

# in the below function it will go to else statement if the value is neither 0 nor 1 and print the factorail .
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    

print(factorial(4))