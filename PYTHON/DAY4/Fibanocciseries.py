# n=int(input("Enter the number : "))
# c=0
# a=0
# b=1
# if n==1 or n==0 :
#     print(1)
# else:
#     for i in range(1,n):
#         c=a+b
#         a=b
#         b=c
#     print(c)
def climbingStars(n):
    if n == 1 or n == 0:
        return 1
    return climbingStars(n-1)+climbingStars(n-2)


print
