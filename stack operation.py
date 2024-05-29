def push(stack,ele):
    stack.append(ele)
    print(ele,"successfully inserted into the stack")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"Deleted successfully")
    stack.pop()
    pop(stack)

stack=[]
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)


pop(stack)
print(stack)
