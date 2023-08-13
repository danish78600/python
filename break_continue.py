# break and continue are also used in python. continue used to skip the iteration and break is used to exit the iteration

# a=0
# while(a<10):
#     print(a)
#     a=a+1
#     if(a==8):
#         break  # this will exit from the loop when the value matches 8

for i in range(10):
    if(i==5):
        continue
    print(i)