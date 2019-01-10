#create multiply function
def multiply(a,b):
	return a*b

#create add function
def add(a,b):
	return a+b

#create subtract function
def subtract(a,b):
	return a-b

#create divide function
def divide(a,b):
	return a/b

#create square function
def square(a):
	return a**2

#create cube function
def cube(a):
	return a**3

#create square_n_times function
def square_n_times(number, n):
	index = 0
	while index < n:
		number = number**2
		index += 1
	return number
	
#add outputs
print("This is the calculator function multiplying 2 and 3")
x = multiply(2,3)
print(x)

print("This is the calculator function adding 3 and 4")
x = add(3,4)
print(x)

print("This is the calculator function subtracting 4 and 5")
x = subtract(4,5)
print(x)

print("This is the calculator function dividing 5 and 6")
x = divide(5,6)
print(x)

print("This is the calculator function squaring 7")
x = square(7)
print(x)

print("This is the calculator function cubing 8")
x = cube(8)
print(x)

print("This is the calculator function squaring 9 three times")
x = square_n_times(9,3)
print(x)