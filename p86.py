def isogram():
	k=input()
	l=list(k)
	r=[]
	for i in l:
		if not i in r:
			r.append(i)
	if len(l)==len(r):
		print('yes');
	else :
		print('no');
try:
	isogram()
except:
	print('invalid');
