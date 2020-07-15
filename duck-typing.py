class A_06():
    def __init__(self):
        super().__init__()
        print("Parent A")

class B_06():
    def __init__(self):
        print("Parent B")

class C_06(A_06,B_06):
    def __init__(self):
        super().__init__()
        print("Child C")

C_06()

#duck typing
class Class1_06():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a+self.b

class Class2_06():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        self.a.append(self.b)
        return self.a

def call(obj):
    print(obj.add())

x=Class1_06(int(input("Enter number 1 : ")),int(input("Enter number 2 : ")))
y=Class1_06(list(input("Enter list 1 : ").split(" ")),list(input("Enter list 2 : ").split(" ")))

call(x)
call(y)
print("\r")
