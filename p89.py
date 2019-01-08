def lex():
	r=input()
	l=list(r)
	l.sort()
	c=''.join(l)
	print(c);
try:
	lex()
except:
	print('invalid');
