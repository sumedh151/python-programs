class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum,salary):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum
        self.salary = salary

    def GetEmployee(self):
        return self.Name() + ", " +  str(self.staffnumber) + "has salary " + str(self.salary)

    def bonus(self,rate=10):
        b=(rate/100)*self.salary
        print("Rate is : ",rate)
        print("Bonus : ",b)
        self.salary=self.salary+b
        print("Updated salary : ",self.salary)

x = Person("Sumedh", "Ghavat")
y = Employee("Sumedh", "Ghavat", 19 , 5000)
