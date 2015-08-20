#!/usr/bin/env python

# Imports

import random

# Body

def welcome():
	
	print "\nLet's play the game of Seventeen!"
	print "Number of marbles left in jar: 17\n"
	

# If the human enters incorrect input (anything other than 1, 2, 3, or a 
# number larger than the number of marbles remaining in the jar), an error 
# message should be displayed, and the human is prompted to try again.

def seventeen(nr_marbles):
	nr_marbles = 17
	while nr_marbles > 0:
		user_input = int(raw_input("\nYour turn: How many marbles will you remove (1-3)? "))
		if user_input <= nr_marbles:
			if (user_input in range(1,4)):
				nr_marbles -= user_input
				print "You removed {0} marbles." .format(user_input)
				if nr_marbles == 0:
					print "There are no marbles left. Computer wins!"
					break
				else:
					print "Number of marbles left in jar:", nr_marbles, "\n"
				

				print "Computer's turn..."
				if nr_marbles > 3:
					x = random.randint (1,3)
				elif nr_marbles == 3:
					x = 2
				elif nr_marbles == 2:
					x = 1
				else:
					x = 1
				
				print "Computer removed {0} marbles." .format(x)
				nr_marbles = nr_marbles - x
				if nr_marbles == 0:
					print "There are no marbles left. Human wins!"
					break
				else:
					print "Number of marbles left in jar:", nr_marbles, "\n"
				
		else: 
			print "Sorry, that is not a valid option. Try again!"
			human_turn(nr_marbles)
	else:
		print "Sorry, that is not a valid option. Try again!"
		human_turn(nr_marbles)

	



def main():

   seventeen(welcome())


if __name__ == '__main__':
    main()