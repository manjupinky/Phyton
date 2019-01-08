import sys
def gcd2():
	(u,y)=map(int,sys.stdin.readline().split())
	while(y!=0):
		t=y
		y=x%y
		u=t
	print(u);
try:
	gcd2()
except:
	print('invalid');
