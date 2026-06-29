def mcCarthy(n):
    if n > 100:
        return n-10
    return mcCarthy(mcCarthy(n+11))


# Driver Mode
n = int(input("Enter a number"))
print("Number : ", mcCarthy(n))
