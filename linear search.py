n=[1,2,3,4,5,6]
target=4
flag=-1
num=len(n)
for i in range(num):
    if n[i]==target:
        flag = i
        break
if flag==-1:
    print("Not found")
else:
    print("Target Found at:", flag)
