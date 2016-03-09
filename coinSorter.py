def float_input(prompt):
	"""Accepts a promt for the user as a string, returns their answer as a float
	Allows user to try again. """
	userNumber = input(prompt)
	finalNumber = None
	while finalNumber != userNumber:
		try:
		#checks if its a number
			userNumber = float(userNumber)
		#only put lines that you expect to cause exceptions here
			finalNumber = userNumber
		except ValueError:
			userNumber = input("That is'nt a valid answer, try again:")
	
	return userNumber



number = float_input("How much money do you have?")

number = int(number)
ogNumber = number
quarter = int(number/25)
number = number%25
dime = int(number/10)
number = number%10
nickle = int(number/5)
number = number%5
penny = int(number/1)
print("{} cents is {} quarter(s), {} dime(s), {} nickle(s), and {} pennies.".format(ogNumber, quarter, dime, nickle, penny))