s=int(input("enter the no"))
r=int(input("enter the no"))
flag=0
c=s*r

for i in range(0,c+1):
    if(i**2==c):
      flag=flag+1


if(flag==1):
    print("yes")
else:
    print("no")
