b=int(input("Enter any number:"))
for i in range(0,b):
  num=2**i
  if num>b:
    print(num)
    break
if b==2:
  print("4")
elif b==1 or b==0:
  print("2")
