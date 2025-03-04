####    ______ COUNTRY TABLE_______
# import mysql.connector as ms
# mysb = ms.connect(host="localhost", user="root", password="password")
# cur = mysb.cursor()
# cur.execute("create database  if not exists Elvish")
# mysb.commit()

# import mysql.connector as ms
# mydb = ms.connect(host="localhost", user="root", password="password")
# cur = mydb.cursor()
# cur.execute("show databases")
# for i in cur:
#     print(i)

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# s1="INSERT INTO country (id, name, key_id, zip_code) VALUES(%s,%s,%s,%s)"
# b1=[(1, 'United States', 'US', 10001),
# (2, 'Canada', 'CA', 20001),
# (3, 'Mexico', 'MX', 30001),
# (4, 'Germany', 'DE', 40001),
# (5, 'France', 'FR', 50001)]
# cur.executemany(s1,b1)
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("select *from country")
# result=cur.fetchmany(5)
# for r in result:
#     print(r)

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("update country set name='America' where id=1")
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("select Sum_Matrix(zip_code),count(distinct name)from country")
# result=cur.fetchall()
# for r in result:
#     print(r)


# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("select *,max(id),Sum_Matrix(zip_code)from country group by name order by id asc")
# result=cur.fetchall()
# for r in result:
#     print(r)

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("ALTER TABLE country CHANGE name country_name VARCHAR(255)")
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("desc country")
# result=cur.fetchall()
# for r in result:
#     print(r)

# ###  _______ STUDENT TABLE_____


# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("create table student(id int(12) primary key,name varchar(23) not null, teacher varchar(23) not null,code int(23) not null)")
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# S1='INSERT INTO student (id, name, teacher, code) VALUES(%s,%s,%s,%s)'
# b1=[(1, 'Alice', 'Mr. Smith', 101),
# (2, 'Bob', 'Mr. Smith', 102),
# (3, 'Charlie', 'Mrs. Johnson', 103),
# (4, 'David', 'Mrs. Johnson', 104),
# (5, 'Eve', 'Mr. Brown', 105),
# (6, 'Frank', 'Ms. White', 106)]
# cur.executemany(S1,b1)
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password'
#                 ,database="Elvish")
# cur=mydb.cursor()
# cur.execute("select *from student")
# result=cur.fetchall()
# for r in result:
#     print(r)

# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# cur.execute("DESC country")
# result = cur.fetchall()
# for r in result:
#     print(r)
# mydb.commit()

###  ________TEACHER TABLE_________


# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# sql='CREATE TABLE teacher (id INT prIMARY KEY,name VARCHAR(100),subject VARCHAR(100),experience varchar(23) not null)'
# cur.execute(sql)
# mydb.commit()

# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# cur.execute("alter table teacher modify experience int(23) not null")
# mydb.commit()

# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# s1="INSERT INTO teacher (id, name, subject, experience) VALUES(%s,%s,%s,%s)"
# b1=[(1, 'Alice Smith', 'Mathematics', 5),
# (2, 'Bob Johnson', 'Science', 7),
# (3, 'Carol Williams', 'History', 4),
# (4, 'David Brown', 'Literature', 10),
# (5, 'Eva Davis', 'Art', 3)]
# cur.executemany(s1,b1)
# mydb.commit()

# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root',
# password='password', database="Elvish")
# cur = mydb.cursor()
# cur.execute("select *from teacher")
# result=cur.fetchall()
# for r in result:
#     print(r)

# import mysql.connector as ms
# mydb = ms.connect(host='localhost',
# user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# cur.execute("update teacher set name='dev sharma' where id=2")
# mydb.commit()

####     ___________ RESULT TABLE______


# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root',
#  password='password', database="Elvish")
# cur = mydb.cursor()
# cur.execute("CREATE TABLE result (id INT prIMARY KEY,teacher_id INT,student_name VARCHAR(100),grade CHAR(2),FOREIGN KEY (teacher_id) REFERENCES teacher(id))")
# mydb.commit()

# import mysql.connector as ms
# mydb = ms.connect(host='localhost', user='root', password='password', database="Elvish")
# cur = mydb.cursor()
# bones=[(1, 1, 'John Doe', 'A'),
# (2, 2, 'Jane Roe', 'B'),
# (3, 3, 'Tom Hanks', 'C'),
# (4, 4, 'Emily Blunt', 'A'),
# (5, 5, 'Chris Evans', 'B')]
# cur.executemany("INSERT INTO result (id, teacher_id,student_name, grade) VALUES(%s,%s,%s,%s)",bones)
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',
# user="root",password='password',database='Elvish')
# cur=mydb.cursor()
# cur.execute("select *from result")
# result=cur.fetchall()
# for r in result:
#     print(r)

###________CUSTOMER TABLE______


# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password',
# database='Elvish')
# cur=mydb.cursor()
# cur.execute('''create table customer
# (id int(23) primary key,
# name varchar(50) not null,
# age int(3) not null,
# email varchar(100) not null,
# fees_amount int(3) not null
# )''')
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',
# password='password',
# database='Elvish')
# cur=mydb.cursor()
# s1="INSERT INTO customer (id, name, age, email, fees_amount) values(%s,%s,%s,%s,%s)"
# b1=[(1, 'John Doe', 28, 'john.doe@example.com', 100),
# (2, 'Jane Smith', 34, 'jane.smith@example.com', 200),
# (3, 'Sam Brown', 22, 'sam.brown@example.com', 150),
# (4, 'Emily Davis', 30, 'emily.davis@example.com', 180),
# (5, 'Michael Johnson', 27, 'michael.johnson@example.com', 130)]
# cur.executemany(s1,b1)
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password',
# database='Elvish')
# cur=mydb.cursor()
# cur.execute("select *from customer")
# result=cur.fetchall()
# for r in result:
#     print(r)

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password',
# database='Elvish')
# cur=mydb.cursor()
# cur.execute("update customer set age=33 where id<>2")
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password',
# database='Elvish')
# cur=mydb.cursor()
# cur.execute("alter table customer change fees_amount fees int(23)")
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password='password',
# database='Elvish')
# cur=mydb.cursor()
# cur.execute(" desc customer")
# mydb.close()


# ### ______ TABLE TOYS_____##########


# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password="password",
#                 database='Elvish')
# cur=mydb.cursor()
# cur.execute('''CREATE TABLE toys (
#     toy_id INT prIMARY KEY,
#     toy_name VARCHAR(50),
#     category VARCHAR(50),
#     material VARCHAR(50),
#     price DECIMAL(10, 2),
#     stock_quantity INT,
#     age_group VARCHAR(20))''')
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password="password",
#                 database='Elvish')
# cur=mydb.cursor()
# s1="INSERT INTO toys (toy_id, toy_name, category, material, price, stock_quantity, age_group) values(%s,%s,%s,%s,%s,%s,%s)"
# b1=[(1, 'RoboDog Ball', 'Interactive', 'Plastic', 29.99, 50, '3-8 years'),
# (2, 'Cat Laser Chase', 'Electronic', 'Metal', 19.99, 100, '4+ years'),
# (3, 'Squeaky Bone', 'Chew Toy', 'Rubber', 9.99, 200, 'All Ages'),
# (4, 'Birdie Swing', 'Exercise', 'Wood', 15.49, 75, '2-5 years'),
# (5, 'Hamster Maze', 'Puzzle', 'Plastic', 22.99, 40, '1+ year')]
# cur.executemany(s1,b1)
# mydb.commit()

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password="password",
#                 database='Elvish')
# cur=mydb.cursor()
# cur.execute("SELECT * FROM toys")
# result=cur.fetchall()
# for row in result:
#     print(row)


# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password="password",database='Travel')
# cur=mydb.cursor()
# sql="insert into passengers(tno,name,start,end)values(%s,%s,%s,%s)"
# val=[("T1","RAVI KUMAR",'DELHI','MUMBAI'),
#      ('T2','NISHANT JAIN','DELHI','KOLKATA'),
#      ('T3','DEEPAK PRAKASH','MUMBAI','PUNE'),
#      ]
# cur.executemany(sql,val)
# mydb.commit()
# print("Done")

# import mysql.connector as ms
# mydb=ms.connect(host='localhost',user='root',password="password",database='Travel')
# cur=mydb.cursor()
# cur.execute("SELECT * FROM passengers")
# result=cur.fetchall()
# for r in result:
#     print(r[1])

# def change(a):
#     s=0
#     for i in range(len(a)//2):
#         s+=(a[i]*2)
#     return s
# B=[10,11,12,30,32,34,35,38,40,2]
# print('OUTPUT IS',change(B))
