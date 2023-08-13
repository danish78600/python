# doctring vs comments 
# comments are description that help programmers ignored by interpreter
# doctrings are right above the function definition

# pep-8 is that which provides guidelines to make python programm readable mainrainable etc.
# pep-python enhancement purposel

# doctring are the string literal that appears at the right of the function,variable etc to give its definition
# these are not comments they are always put above the body
def avg():
    '''this function calculates average'''
    print("avergae")

avg()
print(avg.__doc__)