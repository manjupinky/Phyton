def str1to2():
	g=input()
	l=list(g)
	(e,o)=('','')
	for i in range(len(l)):
		if i%2==0:
			e+=l[i]
		else :
			o+=l[i]
	print(e,o);
try:
	str1to2()
except:
	print('invalid');
