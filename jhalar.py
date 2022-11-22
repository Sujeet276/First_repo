s=int(input("enter the number to draw pattern: "))
print(type(s))
for i in range(s):
    for x in range(1,s+1):
        print(" "*i,end="")
        print("* "*(s-i),end="")
        print(" "*i,end="")
    print("")