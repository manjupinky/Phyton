def lcm2():
	(f,z)=map(int,sys.stdin.readline().split())
	temp=min(f,z)
	while(True):
		if temp%f==0 and temp%z==0:
			break
		temp+=1
	print(temp);
try:
	lcm2()
except:
	print('invalid');
