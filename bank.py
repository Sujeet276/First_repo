import sys
import time
class Customers:
    bankname="mybank"
    def __init__(self,name,balance=0.0):
        print("Welcome to my bank")
        print("welcome {} on my bank".format(name))
        self.balance=balance

    def deposit(self,balance):
        self.balance=self.balance+balance

    def withdraw(self,balance):
        if balance > self.balance:
            print("you have insufficient balance")
            sys.exit()
        else:
            self.balance=self.balance-balance
        
    def showbalance(self):
        print("your account balance is {}".format(self.balance))

name=input()
s=Customers(name)
while True:
    print("choose option for further transaction:")
    print("1. withdraw\n2. deposit\n3. exit\n4. showbalance")
    tem=int(input())
    if tem==1:
        s.withdraw(int(input("enter the amount to withdraw :")))
    elif tem==2:
        s.deposit(int(input("enter the amount to deposit: ")))
    elif tem==4:
        s.showbalance()

    elif tem==3:
        sys.exit()
    print(time.process_time())
        
