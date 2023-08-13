# when we want to collect the values that are not repeated then list is used
# set is a collection of well defined objects the values are put inside{} and are seperated by commas
# the order of the set is not always maintained sets are unchangable and donot contain duplicate items
s={2,4,4,6} 
print(s)

# same as list and tuple in set we can contain multiple values of diff data types.
s1={1,"danish",10,"danish"}
print(s1)

# the below code will return dictionary as both set and dict are denoted by {} 
# so to represent an empty set we can use set()

# danish={} # this code will return dict
danish=set()
print(type(danish))

#SETS METHOODS

# sets work same as in maths
n={1,2,3,4}
m={4,98,7,6}
add=(n.union(m))
n.update(m)  # add the values of m in n whihc are not in n
print(n)
print(add)
both=n.intersection(m)  # the values which are both in n and m will print
print(both)