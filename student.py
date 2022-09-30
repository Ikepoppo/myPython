import time
class Student:
	def __init__(self):
		self.fname = ""
		self.lname = ""
		self.ssn = ""
		self.email = ""
		self.age = ""

	def getfname(self):
		return self.fname

	def getlname(self):
		return self.lname

	def getssn(self):
		return self.ssn

	def getemail(self):
		return self.email

	def getage(self):
		return self.age

	def setfname(self, fname):
		self.fname = fname

	def setlname(self, lname):
		self.lname = lname

	def setssn(self, ssn):
		self.ssn = ssn
	
	def setemail(self, email):
		self.email = email

	def setage(self, age):
		self.age = age

def main():
	t1 = time.time()
	Students = []
	f = open("InsertNames.txt","r")
	for i in f:
		i = i.split(" ")
		student = Student()
		student.setfname(i[0])
		student.setlname(i[1])
		student.setssn(i[2])
		student.setemail(i[3])
		student.setage(i[4])
		matched = False
		for s in Students:
			if s.getssn() == student.getssn():
				print("Error: The SSN is the same as previous student:",i[2])
				matched = True
				break
		if matched == False:
			Students.append(student)
	t2 = time.time()
	t = t2 - t1
	print("Time is : ", t)

main()
