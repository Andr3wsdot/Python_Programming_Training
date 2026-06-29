N = list(map(int, input("Enter The Numbers").split()))
even = 0
odd = 0
for i in N:
    if i % 2 == 0:
        even = even+1
    else:
        odd = odd+1
print(f"{even} even numbers")
print(f"{odd} odd numbers")
