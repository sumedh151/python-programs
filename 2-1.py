#THIS IS USED FOR SINGLE LINE COMMENTS
#WE USE “““...””” and keep them unassigned as multi line comments don’t #exist


from math import *
#imports everything from package math
#integer

a=19
print("a :",a)
print("Type : ",type(a))
print("Binary : {0:b}".format(a))
print("Hex : {0:x}".format(a))
print("Octal : {0:o}".format(a))
#complex
a=2+3j
print("Complex a : ",a)
print("Type : ",type(a))

#floating point with precision
a=3.4245356554798039245
print("\n\nNew a : ",a)
print("Type : ",type(a))			
print("{:2.3f}".format(a))		

#Floor and Ceiling value
print("Ceil : ",ceil(a))			
print("floor : ",floor(a))			

#Other Math
print("Round : ",round(a))
print("Absolute : ",abs(a))		


#Logarithmic
print("Log :",log(a))
print("Log base 10: ",log(a,10))


#Exponent
print("Exponent: ",exp(a))
print("Square: ",pow(a,2))
print("Square Root: ",sqrt(a))

#Trigonometric
print("Sine : ",sin(a))
print("Cosine : ",cos(a))
print("Tangent : ", tan(a))
print("Hyperbolic Sine : ",sinh(a))
print("Hyperbolic Cosine : ",cosh(a))
print("Hyperbolic Tangent : ",tanh(a))
print("Mod : ",modf(a))


 #cmp function has been discarded in python 3
print("Compare : ",(a>4)-(a<4))
print("Maximum : ",max(a,12))
print("Minimum : ",min(a,12))
print("Pi: ",pi)
print("Exponent", e)
print("Degrees : ",degrees(a))
a=45.43
b=30
print("\n\n new a : ",a)
print("b : ",b)
print("{0} + {1} : ".format(a,b),(a+b))
print("{0} - {1} : ".format(a,b),(a-b))
print("{0} * {1} : ".format(a,b),(a*b))
print("{0} / {1} : ".format(a,b),(a/b))

