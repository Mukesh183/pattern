name="mukesh"
def add(no1,no2):
	return no1+no2

def display():
	pass

def test():
	print("Hi")

print(add(10,20))
test()

#factorial
def factorial(no):
	fact=1
	while no>=1:
		fact = fact * no
		no-=1
	else:
		print(fact)

for no in range(5,0,-1):
	factorial(no)

#calculator
#positional arguments
def calc(no1,no2):
	add = no1+no2
	sub=no1-no2
	return add,sub
r1,r2=calc(200,20)
print(r1)
print(r2)

#keywords arguments
def add(n1,n2,n3):
	print(n1)
	print(n2)
	print(n3)
#add(n1=100,n2=200)
#add(n2=100,n1=200)
#add(100,n1=200)
#add(100,n2=200,2)

#default arguments
def add(n1,n2=0):
	print(n1)
	print(n2)
#add(n1=100,n2=200)
#add(100)
#add(n2=100,n1=200)
#add(100,n1=200)

#default arguments
def login(user_name='admin'):
	print(user_name)
login('aaa')
login()

#variable length arguments(*n-->tuple,**n-->dict)
def add(n2=1,*n):
	total=0
	for no in n:
		total+=no
	else:
		print(total)
add()
add(10)
add(111,21)
add(1,2,3,4)

#keywordargs
def add(**n):
	for k, v in n.items():
		print(k, v)
add(name="bcd",age=11,gender=True) 

#Recursion function
#stack method used
def fact(no):
	if no == 1:
		return 1
	else:
		return no * fact(no-1)
print(fact(5))

def add(no):
	if no==1:
		return 1
	else:
		return no+add(no-1)
print(add(2))

def isprime(no,div):
	if no%div==0:
		return False
	else:
		div+=1
		return isprime(no,div)
print(isprime(93,2))



























