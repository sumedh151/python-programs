import mysql.connector

# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sumedhdg15"
#     )

# cursor=db.cursor()

# CREATE NEW DATABASE
# cursor.execute("CREATE DATABASE exp6_19")
# db.commit()
# cursor.execute("SHOW DATABASES")
# for d in cursor:
#     print(d)
# print(" ")

# CREATE TABLES
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sumedhdg15",
    database="exp6_19"
)
cursor =db.cursor()

# cursor.execute("CREATE TABLE users(UserId int primary key,Name varchar(100) NOT NULL,MobileNo numeric(10),City varchar(50) NOT NULL) ")

# cursor.execute("CREATE TABLE train(TrainNo int primary key,TrainName varchar(50),_Source varchar(20),_Destination varchar(20));")
# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)

# #INSERT STATEMENT
# sql="INSERT INTO users(UserId,Name,MobileNo,City) values(%s,%s,%s,%s)"
# l1=list()
# for i in range(1,11):
#     l1.append((str(i),"name"+str(i),str(9000000000+i),"city"+str(i)))
# cursor.executemany(sql,l1)
# db.commit()

# sql="INSERT INTO train(TrainNo,TrainName,_Source,_Destination) values(%s,%s,%s,%s)"
# l1=list()
# for i in range(1,11):
#     l1.append((str(i),"Train"+str(i),"Source"+str(i),"Destination"+str(i)))
# cursor.executemany(sql,l1)
# db.commit()

# #SELECT STATEMENT
# sql="SELECT * from users "
# cursor.execute(sql)
# for values in cursor.fetchall():
#     print(values)

# #WHERE CLAUSE
# sql="SELECT UserId from users where MobileNo>=9000000005"
# cursor.execute(sql)
# for values in cursor.fetchall():
#     print(values)

# #UPDATE TABLES
# sql="UPDATE users set MobileNo = 8976665542 where UserId > 7"
# cursor.execute(sql)
# db.commit()

# # DELETE ROW
# sql="delete from users where UserId =10"
# cursor.execute(sql)
# db.commit()

# print(cursor.rowcount," row/rows deleted")

# # LIMIT AND OFFSET
# sql="SELECT * from users LIMIT 5"
# cursor.execute(sql)
# for values in cursor.fetchall():
#     print(values)
# print("\n")
# sql1="SELECT * from users LIMIT 5 OFFSET 2"
# cursor.execute(sql1)
# for values in cursor.fetchall():
#     print(values)

# DROP TABLE 
sql="DROP TABLE IF EXISTS users"
cursor.execute(sql)
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
