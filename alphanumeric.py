s=input('enter the string:')
p=""
d=""
o=""
for i in s:
    if i.isalpha():
        if p!="":
            if d!="":
                o=o+p*int(d)
                d=""
                p=""
                p=i
            else:
                o=o+p
                p=i
        else:
            p=i
            d=""
    else:
        d=d+i
o=o+p*int(d)
print(o)