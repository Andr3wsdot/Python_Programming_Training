
def isPalindrome(x) :
    y=0
    if x<0 or (x%10==0 and x !=0):
        return False
    while x>y:
        digit=x%10
        y=y*10+digit
        x//=10

    return x==y or x==y//10
x=414
print(isPalindrome(x))