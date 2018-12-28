
try:
	j=int(input())
	flag=0
	for i in range(2,int(j/2)+1):
		if j%i ==0:
			flag=1
			break
	if flag==0:
		print('prime')
	else :
		print('not prime')
except:
print('invalid')
