v=int(input("Enter any number:"))
for i in range(0,v):
  num=2**i
  if num>v:
    print(num)
    break
if v==2:
  print("4")
elif v==1 or v==0:
  print("2")
