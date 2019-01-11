def sumall():
	g=int(input())
	l=[]
	sum=0
	for i in range(g):
		l.append(int(input()))
		sum+=l[i]
	print(sum);
try:
	sumall()
except:
	print('invalid');
