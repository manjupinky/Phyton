 def odddig():
	k=int(input())
	r=[]
	while(k!=0):
		r.append(k%10)
		k//=10
	for i in range(len(r)-1,-1,-1):
		if r[i]%2!=0:
			print(r[i])
try:
	odddig()
except:
	print('invalid')
