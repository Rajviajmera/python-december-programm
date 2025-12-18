# List Comprehension 
#------------> noramal LIST <------------
list1=[2,4,6,8,10]
value=[val **3 for val in list1]
print(value)

#-----------> By Using LOOP <-------------
list2=[1,2,3,4,5,6]
value2=[]
for i in list2:
	value2.append(i*2)
print(value2)

# ---->>>Example Explanation:-> value3 = [j * 2 for j in list3] 
#use list comprehension to create a new list by (doubling) each number in a 
# In place 2 anything can be witten (2 means doublind,3 mean thriple ,...etc.)<<<-----
list3=[1,3,5,7,4]
value3=[j *3 for j in list3]
print(value3)


#------>>> Only EVEN Number list from old list <<<--------
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
v1=[k for k in l1 if k%2==0]
print(v1)


#------->> Create a LIST form Range <<--------
a=[l for l in range(15,0,-1)]
print(a)


#--------->> Using nested loops <<----------
b=[(x,y) for x in range(4) for y in range(5)]
print(b)


#---------->> Flattening a list of lists <<------------
mat=[[1,2,3,11],[4,5,6],[7,8,9,10]]
c=[m for p in mat for m in p]
print(c)