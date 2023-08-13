# A "For" Loop is used to repeat a specific block of code a known number of times

# 2 type of loops:
# for loop
# while loop

# for loop can iterates over a sequence of iterable objects 

# while loop executes till the condition is true when the condition becomes false then it will come out of the while loop

# depending on the while loop condition we have to need either increment or decrement operator

# Python doesn't have do-while loop.


# name="abhishek"
# for i in name:
#     print(i)
#     if(i=="b"):
#         print("this is something special")

# colors=["blue","red","green"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
    
# for k in range(10):
#     print(k)

# for i in range(8,10):
#     print(i*2)

# range function will starts from 8 and prints till 10

# for i in range(0,20,2):
     # range function takes 3 args 1st-starting 2nd-ending 3rd-step 
    # print(i)


#WHILE LOOPS
# a=0
# while(a<=10):
#     print(a)
#     a=a+1

# b=10
# while(b>0):
#     print(b)
#     b=b-1
# else:
#     print("you failed now")

#we can also use else with while loop as when the iteration comes outside while then it will print else statement

# we can also use else statemnet with for loops

for i in range(4):
    print(i)

else:
    print("khtm tata by by")

# in the above code when all the iterations are executed then it will execute the else statemnt

for i in range(6):
    print(i)
    if(i==4):
        break

else:
    print("khtm hogya main bhaijaaaan")

# the above else will not executed as the loop is finished

