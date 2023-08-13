# this enables us to file handling
f=open("d.txt",'w')

# text=f.read() # use to read text file and to extract it
# print(text)
# f.close()


# write

# f.write("hello")
# f.close()

# append
# f.write(" i am danish")
# f.close()

# we can also use this - by using with we donot need to close the f
# with open("d.txt",'a'):
#     f.write("iside with")


# other methods 

# while True:
#     a=f.readline()  # it will read line by line
#     print(a)
#     if not a:
#         break

# writelines will write line one by one and if the given file is not created then it will creates a new one
#In Python, seek() function is used to change the position of the File Handle to a given specific position

