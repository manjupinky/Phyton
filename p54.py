a = map(int,list(str()))
b = map(int,list(str()))
print "a :",a
print "b :",b

l= []
for p,q in zip(a,b):
    l.append(p*q)
print "prod list :",l
ls = sum(l)
print "sum :",ls
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10
top = roundup(ls)
print "round value: ",top
val = top-ls
print "val :",val
a.append(val)
print "output :",a

