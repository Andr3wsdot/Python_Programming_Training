a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter C"))
if a>=b and a>=c :
    if b>c :
        print("B is the Second Largest") 
    else :
        print("C is the Second Largest")
elif b>c and b>a :
    if a>c :
        print("A is the second largest")
    else :
        print("C is the second largest")
else :
    if a>b :
        print ("A is the second largest")
    else :
        print("B is the second Largest")