from pymysql import *
con=connect(host="localhost",user="root",database="student",password="Sujeet@123")
cursor=con.cursor()
if con:
    print("connect successfully")
else:
    print("unsuccessful connection")
p=input()
q=int(input())
cursor.execute("""select * from customer where username= "{}" and password={}""" .format(p,q))
s=cursor.fetchall()
print(s)
con.commit()
cursor.close()
con.close()