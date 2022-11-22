n=input("enter the day:")
p=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(end="\n\n")
for i in range(len(p)):
    print("\t",p[i],"   ",end="\t")
    if (8-(p.index(n)-i))<8:
        print("\t",end="")
        c=8-(p.index(n)-i)
    else:
        c=i-p.index(n)+1
    while c<=31:
        print(c,end="\t")
        c+=7
    print()