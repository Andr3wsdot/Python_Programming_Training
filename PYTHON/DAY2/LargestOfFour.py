a = int(input("Enter A"))
b = int(input("Enter B"))
c = int(input("Enter C"))
d = int(input("Enter D"))
if a >= b and a >= c and a >= d:
    print("A is the largest")
elif b >= a and b >= c and b >= d:
    print("B is the largest")
elif c >= a and c >= b and c >= d:
    print("C is the largest")
else:
    print("D is largest")
