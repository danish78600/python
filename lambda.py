# this functions are without naming these fucntions are easy and are short
# these are used for shorter functions 
double=lambda x:x*2
print(double(2))


# name=input("enter name")
nam=lambda x:x
# print(nam(name))


#lambda functions are mainly used when we pass a function to another function
def app(func,x):
    print(func(x))

app(nam,"kartik")