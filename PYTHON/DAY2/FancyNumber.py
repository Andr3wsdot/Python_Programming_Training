n =input("Enter the no")
increasing=True
decreasing = True
for i in range(len(n)-1) :
    if int(n[i+1]) != int(n[i])+1:
        increasing=False
    if int(n[i+1]) != int(n[i])-1:
        decreasing=False
if increasing :
    print("Increasing Fany Number")
elif decreasing :
    print("Decreasing Fancy Number ")
else :
    print("Not A Fancy Number")