nums = [3, 2, 3]
count = 0
candidate = 0
for nums in nums:
    if count == 0:
        candidate = nums
    if nums == candidate:
        count = count+1
    else:
        count = count-1
print(candidate)
