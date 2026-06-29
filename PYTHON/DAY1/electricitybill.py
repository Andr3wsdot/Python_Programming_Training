n=150
if(n<=100 and n>0):
    bill=(n*1.5)
   
elif(n>100 and n<=200):
    bill=(100*1.5 + 100*2.5 )
    
else:
    bill=(100*1.5 + 100*2.5 + 150*4.0 )
print(bill)