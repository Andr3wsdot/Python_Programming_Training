tuple_list=eval(input("Enter the list of tuples :"))
k=int(input("Enter coulmn index k :"))

product=1

for tup in tuple_list:
    product=product*tup[k]

print(f"Product of values : {k}:{product}")