def assignment1():
	print("Assignment 1 Completed")

# assignment1()

def assignment2():
	# execution of a function ends as soon as it reaches ANY return statement
	return "Assignment 2 Completed"

# assignment2_result = assignment2()
# print(type(assignment2_result))
# print(assignment2_result)

def execute_assignment(assignment_number):
	if assignment_number == 1:
		assignment1()	# function call to run the assignment1 function
	elif assignment_number == 2:
		assignment2_result = assignment2()
		print(assignment2_result)
assignment = "" # sets initial value of "assignment" variable - loop will run until assignment equals 'quit'
while assignment != 'quit':
    number = int(input("Choose assignment number:\n> "))
    execute_assignment(number)
    assignment = input("Would you like to quit (type 'quit') or continue (hit ENTER)\n> ")
