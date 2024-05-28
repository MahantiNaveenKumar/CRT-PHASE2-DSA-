class node:
    def __init__(self,data):
        self.data=data
        self.next=None
#object creation
obj1=node(1)
obj2=node(2)
obj3=node(3)
obj4=node(4)
obj5=node(5)
obj6=node(6)
obj7=node(7)


#linking nodes
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
#printing linked list
initialdata=obj1
while initialdata!=None:
    print(initialdata.data,end="-->")
    initialdata=initialdata.next
print("None")
