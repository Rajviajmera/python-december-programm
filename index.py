import time

def fact_rc(x):
	if x==0 or x==1:
		return 1
	else:
		return x * fact_rc(x-1)
for j in range(1,901):
	# Iterative method for factorial
	print("---------------------")
	start_itime=time.time_ns()
	fact_i=1
	for i in range(1,j+1):
		fact_i=fact_i * i
	print("factorial of {} ={}".format(j,fact_i))
	end_itime=time.time_ns()
	total_itime=end_itime - start_itime
	print("Total Time for Iterative method :",total_itime)

	#Recursive method for factorial
	start_rtime=time.time_ns()
	fact_r=fact_rc(j)
	print("factorial of {} ={}".format(j,fact_r))
	end_rtime=time.time_ns()
	total_rtime=end_rtime - start_rtime
	print("Total Time for Recursive method :",total_rtime)
	print("--------------------------------")

	#file Operation
	file=open("sample.txt","a")
	entry="{},{},{},{}\n".format(j,fact_i,total_itime,total_rtime)
	file.write(entry)
	file.close()