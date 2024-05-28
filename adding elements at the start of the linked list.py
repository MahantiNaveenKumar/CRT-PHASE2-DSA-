class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtspecific(head,posotion, ele):
    if position==0:
        return insertathead(head,ele)

    temp = Node(ele)
    index=0
    currentnode=head

    while index!=position -1:
        currentnode=currentnode.next
        index=index+1

    nextnode=currentnode.next
    temp.next=nextnode
    currentnode.next=temp
    return head
    

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAthead(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)
 
# Object creation is happening      
# obj1 = Node(10)
# obj2 = Node(20)
cc# obj3 = Node(30)
# obj4 = Node(40)
# obj5 = Node(50) 
 
# Links establishing in below lines 
# obj1.next = obj2 
# obj2.next = obj3
# obj3.next = obj4 
# obj4.next = obj5 
 
# print linked list 
#10 --> 20 --> 30 --> 40 --> None
 
