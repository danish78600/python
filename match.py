x=int(input("enter no"))
match x:
    case 0:
        print("x is 0")
    case 10:
        print("x is 10")
    case _ if(x==100):
        print("100 is the value")
    case _:
        print("default")
    

# in python break is not neccesary to implement switch case statement.