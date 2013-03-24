#exercise 1

def print_name(name):
	print 'your name : \n%s' %name

def print_rename(name, familyname):
	print_name(name)
	print ('he is from %s family' %(familyname))

print_rename('bruce','lee')


#exercise 2

def print_number(input):
	
	if (input>=0):
		print(input)
	else:
		input=-input
		print(input)

input = raw_input("input number:")
input=int(input)
print_number(input)


#exercise 3

def print_tf(number):

	if (0<number<10):
		print(number+10)
	
	elif(10<=number<100):
		print(number*0.1)
	
	else:
		print("False")

input=raw_input("input number:")
input=int(input)
print_tf(input)


#exercise 4

import math

x1=raw_input("input number: ")
x2=raw_input("input number: ")
y1=raw_input("input number: ")
y2=raw_input("input number: ")

x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)

number=(x2-x1)**2+(y2-y1)**2
l=math.sqrt(number)
print(l)

#exercise 5

word="next people"
e_num=word.count("e")
print(e_num)


#exercise 6

def compare_input(input1):
	for i in range(len(input1)/2):
		if input1[i]==input1[-(i+1)]:
			pass
		else:
			return 0

	return 1


input1=raw_input("input word  ")
compare_input(input1)
result=compare_input(input1)

if result:
	print("same")
else:
	print("different")

