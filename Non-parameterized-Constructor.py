#Parameterized Constructor
class Employee:
	# Constructor - parameterized  
    def __init__(self,name,id):  
        self.id = id;  
        self.name = name;

    def __str__(self):  
        return "ID: {} \nName: {}".format(self.id,self.name)

emp1 = Employee("John",101)
emp2 = Employee("David",102)

print(emp1)
print(emp2)


#Non-parameterized Constructor
class Employee:    
    # Constructor - non parameterized    
    def __init__(self):    
        print("This is non parametrized constructor")

    def display(self,name,id):
        print("ID: {} \nName: {}".format(id,name))

emp = Employee()    
emp.display("John",101)
