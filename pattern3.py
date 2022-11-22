def print_rangoli(size):
    if size==1:
        print("a")
    else:
        for i in range(0,size):
            print("-"*2*(size-i-1),end="")
            for p in range(0,i+1):
                print(chr(96+size-p),"-",sep="",end="")
            for p in range(i,0,-1):
                print(chr(96+size+1-p),sep="",end="")
                if i!=size-1 or chr(96+size+1-p)!=chr(96+size):
                    print("-",end="")
            print("-"*(2*(size-1-i)-1))
        for i in range(1,size):
            print("-"*2*i,end="")
            for p in range(0,size-i-1):
                print(chr(96+size-p),"-",sep="",end="")
            for p in range(size-i,0,-1):
                print(chr(96+size+1-p),"-",sep="",end="")
            print("-"*((2*i)-1))
        

if __name__ == '__main__':
    n = int(input("enter integer: "))
    print_rangoli(n)