import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com")
server.login("test@gmail.com","test")
f1=open("names.txt","r",encoding="UTF-8")
f2=open("body.txt","r",encoding="UTF-8")
f3=open("email.txt","r",encoding="UTF-8")
names=list(f1.read().split("\n"))
email=list(f3.read().split("\n"))
body=list(f2.read().split("\n"))
#print(names,body,email)
for i in range(len(names)):
    m="Hello, "+names[i]+"\n\n"+body[i]+ " "
    server.sendmail("test@gmail.com",email[i],m)   
f1.close()
f2.close()
f3.close()
