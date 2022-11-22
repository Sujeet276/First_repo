n=eval(input("enter the number: "))
for i in range(n):
    x=1
    while(x!=n):
        for p in range(n):
            print(" "*(n-x),end="")
            print("* "*x,end="")
            print(" "*(n-x),end="")
        print("")
        x+=1
    while(x!=0):
        for p in range(n):
            print(" "*(n-x),end="")
            print("* "*x,end="")
            print(" "*(n-x),end="")
        print("")
        x-=1
    
