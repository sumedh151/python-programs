#Bytearray

#Creating bytearray
a1=bytearray("this is a test","UTF-8")
a2=bytearray("this is a test","ASCII")

b=bytearray(4)

c=bytearray([1,2,3,4,5,6])

d=bytearray(i for i in range(10,20,4))

print("a in UTF-8 encoding as a bytearray : ",a1)
print("a in ASCII encoding as a bytearray : ",a2)
print("b : ",b)
print("c : ",c)
print("c[0] : ",c[0])
print("c[1:4] : ",c[1:4])
print("c[1:] : ",c[1:])
c.extend([10,11,12,13])
print("c.extend([10,11,12,13]) : ",c)
print("d : ",d)
print("\r")
 
#range
print("0-10 : ",end=" ")
for i in range(0,10):print(i,end=" ")
print("\r")
print("Table of 2 :",end=" ")
for i in range(0,20,2) : print(i,end=" ")
print("\r")
print("0-10 with step size = 3 : ",end=" ")
for i in range(0,10,3) : print(i,end=" ")
print("\r")
print("10-0 : ",end=" ")
for i in range(10,0,-1):print(i,end=" ")
print("\r")
print("-8 - -1 : ",end=" ")
for i in range(-8,0):print(i,end=" ")
print("\r")
print("Table of -2 : ",end=" ")
for i in range(-2,-21,-2):print(i,end=" ")
print("\r\r")
 
#sets

#Creating set
s1={0,1,2,3,4,5}
s2=set([2,3,4,5,6,7,8])
print("s1 :",s1)
print("s2",s2)
print("Type of s1: ",type(s1))
print("Type of s2: ",type(s2))

#Length
print("Length of s1 : ",len(s1))
print("Length of s2 : ",len(s2))

#Set Properties
print("s1 U s2 : ",s1.union(s2))
print("s1 n s2 : ",s1.intersection(s2))
print("s1 - s2 : ",s1-s2)
print("s2 - s1 : ",s2-s1)
print("Symmetric difference of s1 and s2 : ",s1.symmetric_difference(s2))
print("Symmetric difference of s2 and s1 : ",s2.symmetric_difference(s1))

#Updation and Deletion
s3=s1.copy()
print("s1 copied onto s3 : ",s3)
s1.add(8)
print("On adding 8 to s1: ",s1)
s2.update([0,1],{9,10,11})
print("On using update to s2: ",s2)
s1.update([i for i in range(0,6)])
print("s1 on adding existing elements doesnt add them : ",s1)
x=s1.pop()
print("Popping first element from s1 : ",x)
print("New s1 : ",s1)
s2.remove(4)
print("After removing 4 from s2 : ",s2)
s1.difference_update({1,2,3})
print("After removing [1,2,3] from s1 : ",s1)
s2.clear()
print("Removing everything from s2 : ",s2)
print("\r")
 
#String
str1='this is a string'
print("str 1 : ",str1)
print("type : ",type(str1))
print("length of string : ",len(str1))

#String Slicing
print("str1[6] : ",str1[6])
print("str1[-3] : ",str1[-3])
print("str1[5:10] : ",str1[5:10])
print("str1[1:] : ",str1[1:])
print("str1[:8] : ",str1[:8])
print("str1[::-1] : ",str1[::-1])
print("str1[5::-1] : ",str1[5::-1])
print("str1[-2:2:-1] : ",str1[-2:2:-1])
print("str1[:5:-1] : ",str1[:5:-1])
print("str1[-3:-5:-1] : ",str1[-3:-5:-1])

#String functions
print("str1.upper() : ",str1.upper())
print("str1.lower() : ",str1.lower())
print("str1.capitalize() : ",str1.capitalize())
print("str1.title() : ",str1.title())
print("str1.count(i) : ",str1.count("i"))
print("str1.count(is) : ",str1.count("is"))
print("str1.find(is) : ",str1.find("is"))
print("str1.isnumeric() : ",str1.isnumeric())
print("str1.isalnum() : ",str1.isalnum())
print("str1.split() : ",str1.split())
print("str1.partition(is) : ",str1.partition("is"))
print("str1.swapcase() : ",str1.swapcase())
print("str1.startswith(t) : ",str1.startswith("t"))
print("str1.startswith(T) : ",str1.startswith("T"))
print("str1.startswith(this) : ",str1.startswith("this"))
print("str1.endswith(g) : ",str1.endswith("g"))
print("str1.endswith(G) : ",str1.endswith("G"))
print("str1.endswith(string) : ",str1.endswith("string"))
print("str1.index(is) : ",str1.index("is"))
print("str1.index(is a string) : ",str1.index("is a string"))
print("rindex(is) : ",str1.rindex("is"))
print("str1.rindex(is a string) : ",str1.rindex("is a string"))
print("str1.ljust(50).added string : ",str1.ljust(50)+"added string")
print("str1.replace(is,replaced) : ",str1.replace("is","replaced"))
str2=str1.center(50,"s")
print("str2 = str1.center(50,s) : ",str2)
print("str2.lstrip(s) : ",str2.lstrip("s"))
print("str2.rstrip(s) : ",str2.rstrip("s"))
#print("Encoded String : ",str1.encode(""))
st2="this\tis\ta\ttest"
print("st2 : ",st2)
print("st2.expandtabs(30) : ",st2.expandtabs(30))
t1=("John","adjc","adewc")
newstr=" separator ".join(t1)
print("join([this is another string]) : ",newstr)

