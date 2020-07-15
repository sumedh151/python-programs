n=int(input("Enter n : "))
l=list()
for i in range(0,n):
   l.append(int(input("Enter element : ")))
max=0


for i in l:
   if max<i:
       max=i
print("Maximum of ",l," =",max)
print("\n\n")



#multiplication table
n=int(input("Enter n to generate its table : "))
for i in range(1,11):
   print(n,"*",i,"=",n*i)
print("\n\n")



#calculator
print("Menu : \n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Power\n6.bth Root\n7.Modulous")
c=int(input("Enter your choice : "))
a=float(input("Enter a : "))
b=float(input("Enter b : "))

if c==1:
   print(a,"+",b,"=",a+b)
elif c==2:
   print(a,"-",b,"=",a-b)
elif c==3:
   print(a,"*",b,"=",a*b)
elif c==4:
   print(a,"/",b,"=",a/b)
elif c==5:
   print(a,"^",b,"=",a**b)
elif c==6:
   print(a,"^",1/b,"=",a**(1/b))
elif c==7:
   print(a,"%",b,"=",a%b)
else:
   print("Invalid choice")

#conversion
print("\n\n\n")
print("Menu : \n1.Kilometers - miles\n2.Celsius - Fahrenheit\n3.Miles- Kilometres\n4.Fahrenheit - celsius\n5.Kilograms - pounds\n6.Pounds - Kilograms")
c=int(input("Enter your choice : "))
a=float(input("Enter value : "))

if c==1:
   print(a," in miles : ",a*0.621371)
elif c==2:
   print(a," in fahrenheit : ",((a*1.8)+32))
elif c==3:
   print(a,"in kilometres : ",a*1.60934)
elif c==4:
   print(a,"in celsius : ",((a-32)*5/9))
elif c==5:
   print(a," in pounds : ",a*2.20462)
elif c==6:
   print(a," in kilograms : ",a*0.453592)
else:
   print("Invalid choice")




