m=int(input("Enter a number:"))
tot=0
while(m>0):
    dig=m%10
    tot=tot+dig
    m=m//10
print("The total sum of digits is:",tot)
