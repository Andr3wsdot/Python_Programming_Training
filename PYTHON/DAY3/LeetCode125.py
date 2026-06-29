# valid palindrome
# sample input
# text="racecar"
n = input(" Enter the text")
org = n
l = len(n)
result = ""
for i in range(l-1, -1, -1):
    result = result+n[i]
if result == org:
    print("Palindrome")
else:
    print("Not Palindrome")
# checkpalindrome=input("enter the text:")
# cleaned=""
# for ch in checkpalindrome:
 #   if ch.isalnum():
  #      cleaned+=ch.lower()
# if cleaned==cleaned[::-1]:
 #   print(True)
# else:
   # print(False)
