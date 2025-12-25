def area(x,y=None):
	if y!=None:
		return x*y
	else:
		return(22/7)*x*x

s1=area(2,3)
print(s1)
s2=area(3)
print(s2)