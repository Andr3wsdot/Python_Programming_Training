# day=str(input("Enter the day"))
# num=int(input("Enter the number of attendees"))
# day1=["MON","TUE","WED","THU","FRI","SAT","SUN"]
# if (day==day1[0]==day1[1]==day1[2]==day1[3])and (num>=1000 and num>=700):
#     print("Sucessful")
# elif (day==day1[4]==day1[5]==day1[6]) and (num>=1500):
#     print("Sucessful")
# else:
#     print("Unsucessful")
day=input("Enter the day : ").strip()
attendees=int(input("Enter the numbers of attendees : "))

def classifySucessOfParty(day,attendees):
    weekdays=["MON","TUE","WED","THU"]
    weekends=["FRI","SAT","SUN"]

    if day not in weekdays and day not in weekdays :
        return "Invalid"
    if attendees<0 :
       return "Invalid" 
    if day in weekdays:
        if 700<=attendees<=1000 :
            return "Sucessful"
        else :
            return "Unsucessful"
    if day in weekends:
        if attendees>=1500 :
            return "Sucessful"
        else :
            return "Unsucessful"
    else:
        return "Invalid"    
result = classifySucessOfParty(day, attendees)
print(result)

# day = input("Enter the day : ").strip().upper()
# attendees = int(input("Enter the numbers of attendees : "))

# def classifySucessOfParty(day, attendees):
#     weekdays = ["MON", "TUE", "WED", "THU"]
#     weekends = ["FRI", "SAT", "SUN"]

#     if day not in weekdays and day not in weekends:
#         return "Invalid"

#     if attendees < 0:
#         return "Invalid"

#     if day in weekdays:
#         if 700 <= attendees <= 1000:
#             return "Successful"
#         else:
#             return "Unsuccessful"

#     elif day in weekends:
#         if attendees >= 1500:
#             return "Successful"
#         else:
#             return "Unsuccessful"

# result = classifySucessOfParty(day, attendees)
# print(result)