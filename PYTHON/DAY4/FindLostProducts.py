productIds = list(map(int, input("Enter The Numbers").split()))
all_id = set(productIds)
duplicates = set()
for id in productIds:
    if productIds.count(id) > 1:
        duplicates.add(id)
lost_ids = all_id-duplicates
print("Lost Product IDs:", lost_ids)

# proid=input("enter").split()

# count={}

# for i in proid:

#     if i in count:

#         count[i]+=1

#     else:


#         count[i]=1


# lost=set()

# for i in count:

#     if count[i]==1:


#         lost.add(i)

# print(lost)
