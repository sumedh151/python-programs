class Roll_06:
    name=""
    age=0
    salary=0.0
    n=0
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    @classmethod
    def accept(cls):
        cls.name=input("Enter name : ")
        cls.age=int(input("Enter age : "))
        cls.salary=float(input("Enter salary : "))
        print("Name :{}\nAge:{}\nSalary:{}".format(cls.name,cls.age,cls.salary))
    
    def display(self):
        print("Name :{}\nAge:{}\nSalary:{}".format(self.name,self.age,self.salary))

    def bonus(self,rate=10):
        b=(rate/100)*self.salary
        print("Rate is : ",rate)
        print("Bonus : ",b)
        self.salary=self.salary+b
        print("Updated salary : ",self.salary)

    @staticmethod
    def test(a):
        print("On adding 20 to ",a,"=",a+20)
    
    class Inner_06:
        def innertest(self):
            print("Displayed Inside an Inner Class")

        def salaryDis(self):
            print("Salary : ",Roll_06.salary)    

ob=Roll_06(input("Enter a name : "),int(input("Enter age : ")),float(input("Enter Salary :")))
ob.display()
ob.bonus(rate=30)
print("\r")
Roll_06.accept()
Roll_06.test(34)
x=ob.Inner_06()
x.salaryDis()
