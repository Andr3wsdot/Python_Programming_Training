s=input("Enter The String")
t=input("Enter the 2nd String")
count=0
L=len(s)
for i in s:
    for j in t:
        if i==j:
            count+=1
if count==L:
    print("ANAGRAM")
else:
    print("NOT ANAGRAM")
