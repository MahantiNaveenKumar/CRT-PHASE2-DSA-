def enqueue(q,ele):
    q.append(ele)
    print(ele,"successfully inserted into the Queue")
def dequeue(q):
    if len(q)==0:
        print("Queue is empty")
        return
    print(q[0],"Deleted successfully")
    q.pop(0)

q=[]
enqueue(q,1)
enqueue(q,2)
enqueue(q,3)
enqueue(q,4)
enqueue(q,5)

print(q)

dequeue(q)
print(q)
