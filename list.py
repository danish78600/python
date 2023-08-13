# Lists are used to store multiple items in a single variable. 
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# the items of list are seperated by comma and are enclosed in[]
# list can be changed but tuple cannot be changed and can contain multiple data types values
# indexing of list always starts from 0



# l=[1,2,3,"danish"]
# print(l)
# print(type(l))

# print(l[-2]) # negative indexing
# print(l[len(l)-2])  # positive indexing  
# print(l[1:])
# print(l[0:4:2]) # 3rd parameter is the jump index

# to check if an element is present in list or not 
# if "danish" in l:
#     print("true")
# else:
#     print("no")


# if "anish" in "danish":
#     print("true")

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# the below method will generates list on the fly

# a=[i for i in range(3)]
# print(a)
# print(type(a))

# the below will print all the values which matches the below condition

# ba=[i for i in range(10) if i%2==0]
# print(ba)

#METHODS OF LIST
list=[1,2,3,4,2]
# print(list)
# list.append(10)
# print(list)
# list.sort(reverse=True)
# print(list)
# print(list.index(2)) # print the 1st occurence of 2
# print(list.count(2))
# list.insert(1,100) # insert 100 in 1st index 
# print(list)
# m=list.copy()
# m[0]=0
# print(m)

m=[2,2,2,2] 
list.extend(m)  # m ko kholo or list ke andar daaldo
print(list)

