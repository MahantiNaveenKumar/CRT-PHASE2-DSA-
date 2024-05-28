class student:
    def __init__(self,name,rollnum,javamarks,pythonmarks,mathsmarks):
        self.name=name
        self.rollnum=rollnum
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathsmarks=mathsmarks
obj=student("naveen",501,43,43,45)
print("Student name : ",obj.name)
print("Roll no : ",obj.rollnum)
print("Java Mrx : ",obj.javamarks)
print("Python Mrx : ",obj.pythonmarks)
print("Maths Mrx : ",obj.mathsmarks)
obj1=student("mani",543,78,32,56)
print("Student name : ",obj1.name)
print("Roll no : ",obj1.rollnum)
print("Java Mrx : ",obj1.javamarks)
print("Python Mrx : ",obj1.pythonmarks)
print("Maths Mrx : ",obj1.mathsmarks)
