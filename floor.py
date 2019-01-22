def si():
	(j,n,r)=map(int,sys.stdin.readline().split())
	sii=j*n*r/100
	print(math.floor(sii));
try:
	si()
except:
	print('invalid');
