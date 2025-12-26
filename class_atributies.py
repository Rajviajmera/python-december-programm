class student:
	def __init__(self) :
		self.name=input("enter name:")
		self.Class=input("enter Class:")		
	def show(self):
		print("Name",self.name)
		print("Class",self.Class)

s1=student()
s1.show()
print()
s2=student()
s2.show()