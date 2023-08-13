# tuple stores multiple values and are seperated by comma and are enclosed in ()
# if we will give one value to tuple then it will print the type int
# tuple cannot be changed but we cna add other data type values to it
tup=(1,2,"danish")
# tup[0]=2  # it will throw an error as tuple cnanot be changed
# print(tup)
# print(type(tup))


# if 2 in tup:
#     print("2 is in tuple")

# tup 2 will be a new tuple
# tup2=tup[1:2]
# print(tup2)

# if we want to change the items of tuple then we have to change a list to a tuple and then back it to list

temp=list(tup)
temp.append("danish bhai")
temp.pop(2)
tup=tuple(temp)
print(tup)

# but we cna concatenate two tuple directly
tup1=("d","a","n")
tup2=("i","s","h","h")
tup3=tup1+tup2
print(tup3)

count=tup3.count("h")
print(count)
ind=tup3.index("n")
print(ind)
