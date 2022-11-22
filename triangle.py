n=int(input("enter the number: "))
print(" "*n,"*",sep="")
for i in range(n-1,0,-1):
    print(" "*i,"*"," "*(2*(n-i)-1),"*",sep="")
print("* "*(n+1))

