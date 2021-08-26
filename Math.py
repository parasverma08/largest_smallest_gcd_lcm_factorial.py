#!/usr/bin/env python3

def solve(arg):

	if arg == 1:
		nos = list(map(int, input("Enter the list of numbers :\n").split()))
		if nos[0] > nos[1]:
			first = nos[0]
			second = nos[1]
		else:
			first = nos[1]
			second = nos[0]
		for item in nos[2:]:
			if item > first:
				second = first
				first = item
		return first

	elif arg == 2:
		nos = list(map(int, input("Enter the list of numbers :\n").split()))
		if nos[0] < nos[1]:
			first = nos[0]
			second = nos[1]
		else:
			first = nos[1]
			second = nos[0]
		for item in nos[2:]:
			if item < first:
				second = first
				first = item
		return first

	elif arg == 3:
		x, y = map(int, input("Enter the two numbers :\n").split())
		while(y):
			x, y = y, x%y
		return x

	elif arg == 4:
		x, y = map(int, input("Enter the two numbers :\n").split())
		num = x*y
		while(y):
			x, y = y, x%y
		lcm = num//x
		return lcm

	elif arg == 5:
		x = int(input("Enter the number :\n").strip())
		def factorial(x):
			if x == 1:
				return 1
			else:
				return (x * factorial(x-1))
		return factorial(x)

if __name__ == "__main__":
	options = "1: Largest\n2: Smallest\n3: GCD\n4: LCM\n5: Factorial\n"
	selected = int(input("Select from the given options :\n" + options).strip())
	print(solve(selected))