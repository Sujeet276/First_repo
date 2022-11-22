from pymysql import *
import sys
con=connect(host="localhost",user="root",database="student",password="Sujeet@123")
cursor=con.cursor()
if con:
    print("connect successfully")
else:
    print("unsuccessful connection")


class user:
    def insert(self,username,name,password,cursor):
        self.username=username
        self.name=name
        self.password=password
        self.cursor=cursor
        self.cursor.executemany("insert into customer values(%s,%s,%s)",[(self.username,self.name,self.password)])
        print("account successfully created")
        con.commit()

    def display(self):
        p=self.cursor.fetchall()
        print("username:",self.username)
        print("name:",self.name)
        print("password:",self.password)
        con.commit()

    def check(username,password,cursor):
        cursor.execute("""select * from customer where username="sujeet" and password=12345""")
        s=cursor.fetchall()
        if s==None:
            print("invalid account")
        elif len(s)==1:
            print("you have valid account")    


print("welcome to my bank")
while True:
    print("please select one of the option:")
    print("create account: 1 ")
    print("check account:2")
    print("exit: 3")
    p=int(input("enter the :"))

    if p==1:
        s=user()
        a=input()
        b=input()
        c=int(input())
        s.insert(a,b,c,cursor)
        s.display()

    if p==2:
        a=input()
        b=int(input())
        user.check(a,b,cursor)
    if p==3:
        break

cursor.close()
con.commit()

    
        


