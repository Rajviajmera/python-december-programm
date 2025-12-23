#Run time error
try:
	a=int(input("enter value:"))
	b=int(input("enter value:"))
	c=a/b
	
except ZeroDivisionError :
	print("Denominator can't be Zero")
except ValueError :
	print("Only Integer value are allowed")
else:
	print("{}/{}={}".format(a,b,c))
finally:
	print("exection completed succesfully")

#for factorial
try:
	x=int(input("enter value:"))
	if x<0:
		raise ValueError ("-ve value not allowed")
	else:
		fact=1
		for i in range(1,x+1):
			fact=fact*i
		print("{}!={}".format(x,fact))

#except ValueError as e :
#	print(e)

except ValueError:
	print("something went wrong")

