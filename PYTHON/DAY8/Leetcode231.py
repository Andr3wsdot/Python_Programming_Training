def isPowerOfTwo(n):
    return n>0 and (n&(n-1))==0

x=1
print(isPowerOfTwo(x))