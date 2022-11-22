s=input()
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:
    if i in ['a','e','i','o','u']:
        print(i+':'+str(d[i]))

