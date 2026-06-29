# 0 to 1 = no rain
# 1 to 5 = light rain
# 5 to 10 = moderate rain
# >10 = heavy rain
r= int(input("Enter the category"))
if r==0 and r==1  :
    print("No Rain")
elif r>1 and r<=5 :
    print("Light Rain")
elif r>5 and r<=10 :
    print("Moderate Rain")
else :
    print("Heavy Rain")