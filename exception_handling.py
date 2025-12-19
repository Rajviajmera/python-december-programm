#Run time error
try:
	a=int(input("enter value:"))
	b=int(input("enter value:"))
	c=a/b
	print("{}/{}={}".format(a,b,c))
except ZeroDivisionError :
	print("Denominator can't be Zero")
except ValueError :
	print("Only Integer value are allowed")
finally:
	print("exection completed succesfully")