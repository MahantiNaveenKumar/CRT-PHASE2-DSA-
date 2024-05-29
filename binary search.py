num=[1,2,3,4,6,11,13,12,7,9,10]
num=sorted(num)
flag=-1
target=13
left=0
right=len(num)-1
while left<=right:
    mid=(left+right)//2
    if num[mid]==target:
        flag=mid
        break
    elif num[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag==-1:
    print("Target not found")
else:
    print("Target found at : ",flag)

