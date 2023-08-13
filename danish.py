def name():
    print(__name__)
    print("danish")

func="i am function"
print("i am not inside main so i will be called automatically")

if __name__=="__main__":
    name()

# it means that if only call name in the danish and if you have to access it outside this class then you have to call it from there
# __name__ this means that from where it is printed