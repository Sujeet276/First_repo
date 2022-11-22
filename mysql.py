import pymysql
con=pymysql.connect(host="localhost",user="root",database="student",password="Sujeet@123")
cursor=con.cursor()
if con:
	print("connection successful")
else:
	print("unsuccessful")
p="insert into sujeet values(%s,%s,%s,%s,%s,%s)"
q=[(1,"sujeet",22,"badud","B.T","m"),(2,"yashwant",24,"gwal","B.T","m"),(3,"hitesh",23,"badud","B.T","m"),(4,"baldev",22,"maheshwar","B.T","m")]
cursor.executemany(p,q)
cursor.execute("select * from sujeet")
con.commit()
data=cursor.fetchall()
for i in data:
	print("the roll_no:",i[0])
	print("the name:",i[1])
	print("the age:",i[2])
	print("the addr:",i[3])
	print("the class:",i[4])
	print("the gender:",i[5])
	print()
cursor.close()
con.close()