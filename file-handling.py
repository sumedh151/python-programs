
#Writing onto a file 
f=open("a.txt","w")
s=input("Enter the string to be entered in the file : ")
f.write(s)
f.close()

#reading from a file
f=open("a.txt","r")
f.seek(0)
s=f.read()
print(s)
f.close()

#appending onto a file

f=open("exp5.1","a+")
a=input("Enter the string to be appended : ")
f.write(a)
f.close()

#searching from a file
b = input("Enter a string to be searched : ")
if b in open("a.txt").read():
    print("The string exists")
else:
    print("The string doesnt exist")
f.close()

#deleting content from a file
f = open('a.txt', 'r+')
f.truncate(0) # need '0' when using r+
s=f.read()
print(s)
