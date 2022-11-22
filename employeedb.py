import pymysql
import sys
con=pymysql.connect(host="localhost",user="root",database="sujeet",password="Sujeet@123")
cursor=con.cursor()
if con:
    print("successful connection")
else:
    print("unsuccessful connection")

class Person:
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age 
        self.dob=dob
        #self.dob=self.Dob(dd,mm,yyyy)
        #self.Dob="{}/{}/{}".format(dd,mm,yyyy)
    class Dob:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy

        def show(self):
            print("{}/{}/{}".format(self.dd,self.mm,self.yyyy))
        
    def showdetails(self):
        print("\t\tname:",self.name)
        print("\t\tage: ",self.age)
        #print("\t\tdob:",self.dob.show())
        print("\t\tdob:",self.dob)

class Employee(Person):
    def __init__(self,name,age,dob,sal,eid,cursor):
        super().__init__(name,age,dob)
        self.sal=sal
        self.eid=eid
        self.cursor=cursor
    
    def display(self):
        print("employee details is :")
        self.showdetails()
        print("\t\teid:",self.eid)
        print("\t\tsal:",self.sal)

    def storedb(self):
        p=("""insert into employee values(%s,"%s",%s,"%s",%s)""" %(self.eid,self.name,self.age,self.dob,self.sal))
        self.cursor.execute(p)
        

def create_account():        
    print("enter your details...")
    name=input("enter employee name: ")
    age=int(input("enter employee age: "))
    #dd,mm,yyyy=[int(i) for i in input("enter employee DOB:").split()]
    dob=input("enter employee DOB:")
    eid=int(input("enter employee eid"))
    sal=int(input("enter the employee sal"))
    return name,age,dob,eid,sal

print("\n\n\t\t\twelcome to my bank")
while True:
    print("select one of the option: ")
    print("\t\t1.create account\n\t\t2.retrive details\n\t\t3.exit")
    a=int(input("select option serial no. : "))
    if a==1:
        name,age,dob,eid,sal=create_account()
        c=Employee(name,age,dob,sal,eid,cursor)
        c.display()
        c.storedb()
        con.commit()
    if a==2:
        eid=int(input("enter the employee eid: "))
        name=input("enter the name")
        cursor.execute('''select * from employee where name="%s"and eid="%s"''' %(name,eid))
        p=cursor.fetchall()
        con.commit()
        eid,name,age,dob,sal=p[0]
        s=Employee(name,age,dob,sal,eid,cursor)
        s.display()
    if a==3:
        cursor.close()
        con.close()
        sys.exit()

