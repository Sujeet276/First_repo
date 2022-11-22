s=input("enter the string: ")
t=""
for i in s:
    if(t==""):
        t=i
    elif(t[-1]<=i):
        t=t+i
    elif(t[0]>=i):
        t=i+t
    else:
        for x in range(0,len(t)):
            if(t[x]>i):
                t=t[:x]+i+t[x:]
                break   
print(t)   