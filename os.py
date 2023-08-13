# used to perform operations of operating system such as to copy file etc
import os
# os.mkdir("data")


# the below code will make 20 folders inside data folder

# for i in range(20):
#     os.mkdir(f"data/code{i+1}")

# the below code will rename 20 folders inside data folder

# for i in range(20):
#     os.rename(f"data/code{i+1}" ,f"data/tuts{i+1}")

# to cehck the folder inside data
# folders=os.listdir("data")
# print(folders)

# for i in folders:
#     print(i)

# to check teh cureent directory
dir=os.getcwd()
print(dir)