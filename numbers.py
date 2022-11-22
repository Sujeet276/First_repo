if __name__=="__main__":
    s=int(input('enter the no. less than 100 billion : '))
    p=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    q=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
    r=['billion','million','lakh','thousand','hundred']
    d=[100000000,1000000,100000,1000,100,1]
    h=" "
    t=s
    num=''
    if t==0:
        num='zero'
    x=0
    while t>0:
        z=t//d[x]
        if z!=0:
            if z<20:
                num=num+h+p[z-1]
            else:
                num=num+h+q[z//10-2]
                if z%10!=0:
                    num=num+h+p[z%10-1]
            if t<100:
                t=0
            if t>=100:
                t=t%d[x] 
                num=num+h+r[x]
        x=x+1
    print(num)





        