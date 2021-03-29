class Student:
	def __init__(self, name, rollno, m1, m2):
		self.name = name
		self.rollno = rollno
		self.m1 = m1
		self.m2 = m2
		

	def accept(self, Name, Rollno, marks1, marks2 ):
		 int(input()) 
		 ob = Student(Name, Rollno, marks1, marks2 )
		 ls.append(ob)

	def display(self, ob):
			print("Name : ", ob.name)
			print("RollNo : ", ob.rollno)
			print("Marks1 : ", ob.m1)
			print("Marks2 : ", ob.m2)
			print("\n")	
		
	# Search
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i	

	# Delete						
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	# Update 
	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll;
		
# list to add Students
ls =[]
#object of Student class
obj = Student('', 0, 0, 0)

print ("1. Display")
print ("2. search")
print ("3. Delete")
print ("4. Update")
ch = int(input("Enter choice:"))
 
if(ch == 1):
 obj.accept()


elif(ch == 2):
 print("\n")
 print("\nList of Students\n")
for i in range(ls.__len__()):	
 obj.display(ls[i])
	
elif(ch == 3):
 print("\n Student Found, ")
 s = obj.search(2)
 obj.display(ls[s])
		
elif(ch == 4):
  obj.delete(2)
  print(ls.__len__())
  print("List after deletion")
for i in range(ls.__len__()):	
	obj.display(ls[i])
			
elif(ch == 5):
 obj.update(3, 2)
 print(ls.__len__())
 print("List after updation")
for i in range(ls.__len__()):	
	obj.display(ls[i])
			
else:
print("Thank You !")
	
