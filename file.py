'''f=open("pqrs.txt","a")#w--> overwrite
f.write("Mukesh\n")
f.write("siva\n")
f.write("gowtham\n")
l=["hi","hello"]
f.writelines(l)
f.close()

f=open("pqrs.txt","r")
lines=f.readlines()
for line in lines:
	print(line,end=" ")
print(f.read(1))
print(f.readline())
print(f.read(3))
f.close()

         #(or)

with open("pqrs.txt","r") as f:
	lines=f.readlines()
	for line in lines:
		print(line,end=" ")
	print(f.read(1))
	print(f.readline())
	print(f.read(3))
	f.close()
	
import os
location=input("Enter file name with location: ")
if os.path.isfile(location):
	print("yes present")
	f=open(location,"r")
	linecount=0
	charcount=0
	for line in f:
		charcount+=len(line)
		linecount+=1
	print(linecount)
	print(charcount)
else:
	print("Not Present")#old version

#image read bytes 
f= open("/home/desktop/pythonfolder/a.jpeg","rb")
f2= open("/home/desktop/pythonfolder/b.jpeg","wb")
bytes = f.read()
f2.write(bytes)

import csv
with open ("students.csv", "w",newline='') as f:
	writer=csv.writer(f)
	writer.writerow(["SID","SNAME","SADDRESS"])
	count=int(input("Enter no.of. students "))
	for i in range(count):
		sid=int(input("Enter ID"))
		sname=input("Enter name")
		address=input("Enter address")
		writer.writerow([sid,sname,address])

#reader

import csv
with open ("students.csv", "r",newline='') as f:
	rdr=csv.reader(f)
	l=list(rdr)
	for line in l:
		for word in line:
			print(word,"\t",end=" ")
		print()


import pickle
class Student:
	def __init__(self,sid,sname,saddress):
		self.sid=sid
		self.sname=sname
		self.saddress=saddress
	def display(self):
		print(self.sname)
with open("student.dat","wb")as f:
	s1=Student(101,"abxd","chn")
	pickle.dump(s1,f)

with open("student.dat","rb")as f:
	ob=pickle.load(f)
	ob.display()
'''

'''import os
print("the current working directory:")
print(os.getcwd())

fileName = "Contents.txt"

fileObject = open(fileName, "r+")

 

# Print the full path of the newly created file now

print("Full path of the created file is:")

print(os.path.realpath(fileName))

os.chdir('NewDirectory')
print(os.getcwd())

import os
os.chdir('NewDirectory/sub')
print(os.getcwd())
'''



































	
