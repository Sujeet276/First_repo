def func(n):
    s=["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    p=[]
    if n//10==0:
        return(s[n])
    else:
        for i in func(n//10):
            for j in s[n%10]:
                b=""
                b=i+j
                p.append(b)
        return(p)



n=int(input())
x='\n'.join(map(str,func(n)))
print(x)

