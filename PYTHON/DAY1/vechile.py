a = int(input("No.of vechiles"))
b = int(input("No. of wheels"))
for i in range(a):
    for j in range(a):
        if (i+j == a and (4*i)+(2*j) == b):
            print(i, j)
