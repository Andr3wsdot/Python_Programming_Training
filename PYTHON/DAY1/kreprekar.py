#n=int(input(""))
#m=n**2
#m1=m//100
#m2=m%100
#sum1=m1+m2
#if sum1==n :
#    print("keprakar no.")
#else:
#    print("keprakar no.")
n=int(input("Enter a number"))
square=n*n
digits=len(str(n))
right=square%(10*digits)
left=square//(10**digits)

if left+right==n:
    print("Keprakar no.")
else:
    print("Not Keprakar")