# dictionary is used to store key value pairs as they are ordered collection of data items 

dict={"name":"danish","school":"SSSS"}
print(dict["name"])  # we can also access indivisual object or as whole
print(dict.get("name"))

# both the above print are same but the 2nd one will not throw error if the key does not exists

print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(f"the coresponding value of {key} is {dict[key]}")

print(dict.items())

# methods - dictionary contain multiple built in methods

ep1={1:1,2:2}
ep2={3:3,4:4}
ep1.update(ep2) # the value of ep2 will move inside e1
print(ep1)

# emp={} # empty dict
# ep1.pop(2)
# print(ep1)
# ep1.popitem()  # removes the last element 
# print(ep1)

# del ep1 # it will delete the dictonary if the keys are present

del ep1[1]  # delete the value present in key 1
print(ep1)

