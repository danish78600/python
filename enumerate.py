# marks=[1,2,3,4,5,6,6,7,78,91]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("danish")
#     index=index+1

# to solve the above function's complexity we have to use enumerate

marks=[1,2,3,4,5,6,6,7,78,91]
for index, marks in enumerate(marks,start=1):      # start=1 will change the starting index no
    print(marks)
    if(index==3):
        print("danish")

# with the use of enumerate we will get both the values and indexes at the same time