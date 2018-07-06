"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
	raw_user_input = input(">")
	user_input = raw_user_input.split(" ", 3)
	print(user_input)

	command = user_input[0]
	
	try:
		num1 = user_input[1]
	except:
		continue
	try:
		num2 = user_input[2]
	except: 
		continue
	try:
		num3 = user_input[3]
	except:
		continue

	print(command, num1, num2, num3)
	if command == "q":
		break
	else:
		if command == "+":
			print(add(num1, num2))