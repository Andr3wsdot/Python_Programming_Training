num = list(map(int, input("Enter The Numbers").split()))
k=int(input("Enter the threshold value k:"))
freq=dict()

for i in num :
    freq[i]=freq.get(i,0)+1

for i,count in freq.items():
    if count>k:
        print(f"{num} : {count} times")