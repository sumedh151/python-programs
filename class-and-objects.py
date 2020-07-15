class Dog():    
    species = 'mammal'  #class object attribute

    def __init__(self,name,breed,age,spots):
        self.name = name
        self.breed = breed
        self.age = age
        self.spost = spots
    
    def bark(self):     #class method
        print('WOOF!')

    def display(self):    # class method
        print('WOOF! My name is {} and my age is {}.\n I am a {}'.format(self.name,self.age,self.breed))

    def bit(self,number):     #static method (outside parameter)
        print('WOOF! My name is {} and I\'ve bit {} people'.format(self.name,number))

    class Inner:
        def innertest(self):
            print("Displayed Inside an Inner Class")


pet = Dog('Jim','lab',5,True)
pet.bark()
pet.display()
pet.bit(5)
x=pet.Inner()
x.innertest()
