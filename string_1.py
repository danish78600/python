# string in python is like array of characters so we can print its each character by its index no.

# strings are immutable and cannot be changed but there copy can be changed.

names="danish,shubham"
print(names[0:6])    # it will slice the string as it will print it from 0th index to n-1 string including 0 but not 5 
print(len(names))    # it will print the length of names


# negative slicing
# print(names[0:-10])
# in the 2nd param the python will automatically take len(names)-10

# nm="harry"
# print(nm[-4:-2]) # the 1st means minus 4 from the lenght of string and start from there

# string methods

a="danish bhai jogindar"
# print(a.upper()) # this will not change the exisiting string but will make a new string as strings in python are immutable

# print(a.lower())
# print(a.strip(" "))
# print(a.replace("danish","shubham"))
# print(a.split(" ")) # split converts string into list

print(a.capitalize()) # makes the 1st letter capital and others to lowercase 
print(a.center(10)) # it will change the length of string by increasing its spaces as it moves it toward center
print(len(a))
print(a.count("a")) # how much times a is occuring

print(a.endswith("r")) # prints true if the string is ending with r
print(a.find("a"))  # print the 1st occurence of the string

# islower() isalpha() startswith() etc are many methods in string
# swap() -swaps the string