import sys
 def getl():
	l1=[]
	r2=[]
	while(True):
		try:
			a,b = map(int,sys.stdin.readline().split())
		except ValueError:
			break
		l1.append(a)
		l1.append(b)
		r2.append(l1)
		l1=[]
	for i in r2:
		print(i[1]-i[0])
try:
	getl1()
except:
	print('invalid')
