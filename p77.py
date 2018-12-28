a=int(input("enter the no"))
for i in range(1,a+1):
    if(a%i==0):
        print(i,end=',')
    else:
        print("invalid")
