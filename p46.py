n=int(input("Enter a number: "))
s=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    s.append(i)
print("=",sum(s))
 
print()

