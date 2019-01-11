import sys
def cuboid():
	l2,b2,h2=map(int,sys.stdin.readline().split())
	print(l2*b2*h2)
try:
	cuboid()
except:
	print('invalid')
