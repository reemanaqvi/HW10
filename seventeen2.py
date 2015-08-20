#!/usr/bin/env python

# Imports

import random

# Body


file = open('i206_placein_output2_reema.txt' , 'w')

with open('i206_placein_input.txt') as fin:

	nr_marbles = 17
	for line in fin:
		b = line.strip()
		c = b.split(",")
		while nr_marbles > 0:
			p2 = 0
			for item in c:
				if nr_marbles < item:
					nr_marbles -= nr_marbles
					p2 += 1
					# return p2
				else:
					nr_marbles = nr_marbles - item
					
					file.write(item, '-')
			
				p1 = 0
				if nr_marbles > 3:
					x = random.randint (1,3)
				elif nr_marbles == 3:
					x = 2
				elif nr_marbles == 2:
					x = 1
				else:
					x = 1
				file.write(x)
						
				nr_marbles = nr_marbles - x
				if nr_marbles == 0:
					P1 += 1
					# return p1	

	
		
	

