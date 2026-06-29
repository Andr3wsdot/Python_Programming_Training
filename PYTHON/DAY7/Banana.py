import math
bunch=[3,6,7,11]
h=8
left=1
right=max(bunch)
ans=right
while left<=right:
    mid=left+(right-left)//2
    total_h=0
    for i in bunch:
        total_h=total_h+math.ceil(i/mid)
    if total_h<=h:
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)