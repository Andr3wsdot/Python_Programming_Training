n = int(input("Enter the no . of tickets"))
iprice = float(input("Enter the price of ticket"))
c = int(input("Enter the category"))
tprice = iprice*n
dprice = 0
if c == 1:
    if n >= 15:
        dprice = tprice-(tprice*0.2)
        print("Discount Applied=", dprice)
    else:
        dprice = tprice
        print("Discounted Price=", dprice)
elif c == 3:
    dprice = tprice-(tprice*0.25)
    print("Discounted price", tprice)
elif c == 2:
    dprice = tprice-(tprice*0.05)
    print("Applied Discount", dprice)
else:
    dprice = tprice
    print(dprice)
