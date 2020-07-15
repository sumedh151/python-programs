#array
import array as arr
import random as r

a = arr.array("i",[1,7,3,4,6,9,8,5,2,10,11,12,0])
for i in a :
    print(i,end=" ")

print("\nType of a is: ",type(a))


print("Slicing  dicing of array:")

print("Element at index 1: ",a[1])
print("Element at index 2 to 4 : ",a[2:5])
print("Elements from start to index 4 : ",a[:5])
print("Elements from index 1 to end : ",a[1:])
print("Reverse indexing a[-5] : ",a[-5])


for i in range(0,10):
    a.append(i*3*r.randint(1,11))


print("append() random 10 variables to a : ",a)
a.extend(x*r.randint(1,6) for x in range(1,10))
print("a.extend(x*randint(1,6) for x in range(1,10)) : ",a)
a.insert(4,333333)
print("a.insert(4,333333) : ",a)
print("sum(a) : ",sum(a))
print("a.index(0) : ",a.index(0))
print("a.pop() : ",a.pop())
print("a.pop(4) : ",a.pop(4))
a.remove(4)
print("a.remove(4) : ",a)
a.reverse()
print("a.reverse() : ",a)
print("a.tolist() : ",a.tolist(),"\nType : ",type(a.tolist()))
print("a.count(3) : ",a.count(3))
odd=arr.array("i",list(x for x in range(0,10,2)))
even=arr.array("i",list(x for x in range(1,10,2)))
array1=odd+even
print("concat of odd and even array : ")
print("Odd Array : ",odd)
print("Even Array : ",even)
print("Odd + Even : ",array1)
print("odd * 4 : ",odd*4)


#numpy array
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.int64)
b=np.full((3,3),10)
c=np.array([[1+2j,2+5j,3-4j],[4+4j,5-5j,6+3j],[7,8,9]],dtype=np.complex)
d=np.eye(4)
l=[(1,2,3,4),(4,5)]
x=np.arange(24)
b1=x.reshape(2,4,3)
na=np.asarray(x)
na1=np.linspace(10,20,5)
na2=np.linspace(10,20,5,endpoint= False)
na3=np.linspace(10,20,5,retstep=True)
nn1=np.logspace(1,10,num=10)
nn2=np.logspace(1,10,num=10,base =2)
a1=np.arange(10)
print("\n\nNumpy Arrays:\n a: \n",a)
print("\nb:\n",b)
print("\nc:\n",c)
print("\nd:\n",d)
print("\nnp.arange(24).reshape(2,4,3) : \n",b1)
print("\nnp.asarray(x) : \n",na)
print("\nnp.linspace(10,20,5) : \n",na1)
print("\nnp.linspace(10,20,5,endpoint=False) : \n",na2)
print("\nnp.linspace(10,20,5,retstep=True) : \n",na3)
print("\nnp.logspace(1,10,num=10) : \n",nn1)
print("\nnp.linspace(1,10,num=10,base=2) : \n",nn2)
print("\nnp.arange(10) : \n",a1)
print("Array of 1s of {} : \n {}".format(np.ones((3,4)).shape,np.ones((3,4))))
print("Array of 0s of {} : \n {}".format(np.zeros((5,4)).shape,np.zeros((5,4))))
print("Reshaped array a into 9rows 1 column : \n",a.reshape(9,1))
print("type(a) : ",type(a))
print("a.shape : ",a.shape)
print("a[...,1] : \n",a[...,1])
print("a[1,...] : \n",a[1,...])
print("a[...,1:] : \n",a[...,1:])
print("a[1:,...] : \n",a[1:,...])
print("a[1:,1:] : \n",a[1:,1:])
print("a.ndim : ",a.ndim)
print("a.shape : ",a.shape)
print("a.itemsize : ",a.itemsize)
print("a.data : ",a.data)
print("a.transpose() : ",a.transpose())
#print("a.corrcoef() : ",a.corrcoef())
s=slice(2,7,2)
print("a[slice(2,7,2)] : ",a[s])
x,y=np.mgrid[0:5,1:6]
print("x,y=np.mgrid[0:5,1:6]")
print("x :\n",x)
print("y :\n",y)
print("x+y : \n",x+y)
print("x-y : \n",x-y)
print("x*y : \n",x*y)
z=np.asmatrix(a)
print("Converting array c to matrix : ")
z1=np.asmatrix(c)
print("z1 : \n",z1," \nType : ",type(z1))
print("z1.T : \n",z1.T)
print("z1.H : \n",z1.H)
f=z1.flat
print("z1.flat : ",f)
print("z1.reshape(1,9) : \n",z1.reshape((1,9)))
print("matrix operations : ")
a=np.matrix([[1,2],[3,4]])
b=np.matrix([[-1,-2],[6,7]])
print("a : \n",a)
print("b : \n",b)
print("a+b : \n",a+b)
print("a-b : \n",a-b)
print("a*b : \n",a*b)
print("a**2 : \n",a**2)



