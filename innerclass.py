class sujeet:
    def __init__(self,name,age,rollno,dd,mm,yyyy):
        print("hello! how are you...")
        self.name=name
        self.age=age  
        self.rollno=rollno 
        self.dob=self.dob(dd,mm,yyyy)

    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("age:",self.age)
        self.dob.display()

    class dob:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print("{}/{}/{}".format(self.dd,self.mm,self.yyyy))

s=sujeet("sujeet",22,110,27,6,1999)
s.display()