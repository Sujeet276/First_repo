s=eval(input("enter the element: "))
l=[10,20,30]
p=[]
n=int(input("enter the index position: "))
if n>=len(l):
    l.append(s)
elif n<=0:
    p.append(s)
    p.extend(l)
    l=p
else:
    p=l[:n]
    p.append(s)
    p.extend(l[n:])
    l=p
print(l)

