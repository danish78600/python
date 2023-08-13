# is compares exact location in memory
# == compares value
# a=[1,2,43]
# b=[1,2,43]

a=2
b=2
print(a is b) # this will be true in this a constant is made so python will not create another memory for another 3
print(a ==b)

# tuple will also return true for is condtion as tuple is immutable