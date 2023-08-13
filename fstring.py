# fstrings are used to access varibales inside strings
name="danish"
city="india"
print(f"hey my name is {name} and i live in {city} ")
print(f"hey my name is {name} and i live in {{city}} ") # this code will print city in the brackets

# we can also do by the beloew method but the above one is convinient
letter="hey are you from {0}"
c="bharat"
print(letter.format(c))