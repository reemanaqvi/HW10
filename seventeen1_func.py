#!/usr/bin/env python

# Imports
import sys
import random

# Body

def welcome():
	
	print "\nLet's play the game of Seventeen!"
	print "Number of marbles left in jar: 17\n"
	

# If the human enters incorrect input (anything other than 1, 2, 3, or a 
# number larger than the number of marbles remaining in the jar), an error 
# message should be displayed, and the human is prompted to try again.

def human_turn(marbles_left):
	user_input = raw_input("\nYour turn: How many marbles will you remove (1-3)? ")
	
	try:
		valid_ = user_input in (1,2,3)
	except:	
		print "except:Sorry, that is not a valid option. Try again!"
	else: 
		if (user_input > marbles_left):
			print "else:Sorry, that is not a valid option. Try again!"
		else:
			user_input = int(user_inpsut)
			marbles_left = int(marbles_left - user_input)
			print "You removed {0} marbles." .format(user_input)
			if marbles_left == 0:
				print "There are no marbles left. Computer wins."
				return
			else:
				print "Number of marbles left in jar:", marbles_left, "\n"
			return marbles_left
		

def comp_turn(marbles_left):
	print "Computer's turn..."
	if marbles_left > 3:
		x = random.randint (1,3)
	elif marbles_left == 3:
		x = 2
	elif marbles_left == 2:
		x = 1
	else:
		x = 1
	print "Computer removed {0} marbles." .format(x)
	marbles_left = marbles_left - x
	if marbles_left == 0:
		print "There are no marbles left. Player 1 wins"
		exit(0)
	else:
		print "Number of marbles left in jar:", marbles_left, "\n"
	
	return x



def main():
    marbles_left = 17
    welcome()
    while marbles_left > 0:
    	human_turn(marbles_left)
    	comp_turn(marbles_left)




if __name__ == '__main__':
    main()