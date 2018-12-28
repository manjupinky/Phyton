g=input("Enter your seqence (Mod/Dividee):")
op=['%','/']
for x1 in g:
	if x1 in op:
		if(x1=='%'):
			k1=int(g.split(x1)[0])
			k2=int(g.split(x1)[1])
			ans=k1%k2
		elif(x1=='/'):
			k1=int(g.split(x1)[0])
			k2=int(g.split(x1)[1])
			ans=k1//k2
print(ans)
